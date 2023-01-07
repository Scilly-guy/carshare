import logging

from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils import timezone

from billing.models import BillingAccount, get_billing_accounts_suitable_for_booking
from hardware.models import VehicleType

log = logging.getLogger(__name__)


def gen_start_time(now):
    minutes = now.minute - (now.minute % 5)
    return now.replace(minute=minutes, second=0, microsecond=0) + timezone.timedelta(
        minutes=5
    )


def gen_end_time(now):
    start = gen_start_time(now)
    return start + timezone.timedelta(hours=1)


class VehicleTypeMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class BookingSearchForm(forms.Form):
    start = forms.SplitDateTimeField(
        label="Start time",
        widget=forms.SplitDateTimeWidget(
            date_attrs={"type": "date"},
            time_attrs={"type": "time", "step": "60"},
            date_format="%Y-%m-%d",
            time_format="%H:%M",
        ),
    )
    end = forms.SplitDateTimeField(
        label="End time",
        widget=forms.SplitDateTimeWidget(
            date_attrs={"type": "date"},
            time_attrs={"type": "time", "step": "60"},
            date_format="%Y-%m-%d",
            time_format="%H:%M",
        ),
    )
    vehicle_types = VehicleTypeMultipleChoiceField(
        label="Type of vehicle",
        queryset=VehicleType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        error_messages={"required": "You must select at least one type of vehicle."},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout("start", "end", InlineCheckboxes("vehicle_types"))

        self.fields["vehicle_types"].initial = VehicleType.objects.all()

        now = timezone.now()
        self.fields["start"].initial = gen_start_time(now)
        self.fields["end"].initial = gen_end_time(now)

    def clean_start(self):
        start = self.cleaned_data["start"]

        if start + timezone.timedelta(minutes=5) < timezone.now():
            raise ValidationError("Your booking must not start in the past.")

        return start

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")

        if start and end and start >= end:
            raise ValidationError("You must choose an end time after your start time.")

        if start and end and start + timezone.timedelta(hours=1) > end:
            raise ValidationError("Your booking must be at least 1 hour long.")


class BookingDetailsForm(forms.Form):
    start = forms.DateTimeField(widget=widgets.HiddenInput)
    end = forms.DateTimeField(widget=widgets.HiddenInput)
    vehicle_id = forms.IntegerField(widget=widgets.HiddenInput)
    confirmed = forms.BooleanField(required=False, widget=widgets.HiddenInput)


class ConfirmBookingForm(forms.Form):
    start = forms.DateTimeField(widget=widgets.HiddenInput)
    end = forms.DateTimeField(widget=widgets.HiddenInput)
    vehicle_id = forms.IntegerField(widget=widgets.HiddenInput)
    confirmed = forms.BooleanField(required=False, widget=widgets.HiddenInput)
    billing_account = forms.ChoiceField(required=True, widget=widgets.Select)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if len(args) > 0:
            self.set_billing_accounts(args[0]["end"])

    def set_billing_accounts(self, end_time):
        bas = get_billing_accounts_suitable_for_booking(self.user, end_time)

        choice_list = [("", "--------")]
        for ba in bas:
            if ba.account_type == BillingAccount.PERSONAL:
                label = f"{ba.owner.first_name} {ba.owner.last_name} (Personal)"
            elif ba.account_type == BillingAccount.BUSINESS:
                label = f"{ba.account_name} (Business)"
            else:
                log.error(
                    "Encountered unknown billing account type: {obj.account_type}"
                )
                label = "**unknown**"

            choice_list.append((ba.id, label))

        self.fields["billing_account"].choices = choice_list

    def clean_billing_account(self):
        ba_id = self.cleaned_data["billing_account"]

        if ba_id == "":
            raise ValidationError("Please select a billing account for this booking.")

        try:
            ba = BillingAccount.objects.get(pk=ba_id)
        except:
            raise ValidationError(
                "Please select a billing account you are allowed to make bookings for."
            )

        return ba

    def clean_start(self):
        start = self.cleaned_data["start"]

        if start + timezone.timedelta(minutes=5) < timezone.now():
            raise ValidationError("Your booking must not start in the past.")

        return start

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        ba = cleaned_data.get("billing_account")

        if start and end and start >= end:
            raise ValidationError("You must choose an end time after your start time.")

        if start and end and start + timezone.timedelta(hours=1) > end:
            raise ValidationError("Your booking must be at least 1 hour long.")

        if ba is not None:
            valid_bas = get_billing_accounts_suitable_for_booking(self.user, end)
            if ba not in valid_bas:
                raise ValidationError(
                    "You must choose a billing account you are allowed to make bookings with."
                )
