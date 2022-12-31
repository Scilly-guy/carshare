from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from allauth.account import views

from .decorators import require_incomplete_user
from .forms import (
    SignupForm,
    AddMobileForm,
    VerifyMobileForm,
    LoginForm,
)
from .sms import send_sms_verification_code


@login_required
@require_incomplete_user
def incomplete(request):
    context = {
        "user": request.user,
        "menu": "profile",
    }
    return render(request, "users/incomplete.html", context)


class SignUpView(views.SignupView):
    template_name = "users/signup.html"
    form_class = SignupForm


class LoginView(views.LoginView):
    template_name = "users/login.html"
    form_class = LoginForm


class EmailVerificationSentView(views.EmailVerificationSentView):
    template_name = "users/email_verification_sent.html"


class ConfirmEmailView(views.ConfirmEmailView):
    template_name = "users/confirm_email.html"


@login_required
def add_mobile(request):
    if request.method == "POST":
        form = AddMobileForm(request.POST, instance=request.user)
        if form.is_valid():
            u = form.save()
            send_sms_verification_code(u.mobile_verification_code, u.pending_mobile)
            return redirect("users_mobile_verify")
    else:
        form = AddMobileForm(instance=request.user)

    context = {"menu": "profile", "form": form}

    return render(request, "users/add_mobile.html", context)


@login_required
def verify_mobile(request):
    if request.method == "POST":
        form = VerifyMobileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users_incomplete")
    else:
        form = VerifyMobileForm()

    context = {
        "menu": "profile",
        "form": form,
    }
    return render(request, "users/verify_mobile.html", context)


@login_required
def profile_my_details(request):
    context = {
        "menu": "profile",
        "profile_menu": "details",
    }

    return render(request, "users/profile_my_details.html", context)
