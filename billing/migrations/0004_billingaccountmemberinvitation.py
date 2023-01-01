# Generated by Django 4.1.3 on 2022-12-30 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("billing", "0003_billingaccount_business_address_line_1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingAccountMemberInvitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("can_make_bookings", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                ("secret", models.UUIDField()),
                ("create_at", models.DateTimeField()),
                (
                    "billing_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invitations",
                        to="billing.billingaccount",
                    ),
                ),
                (
                    "inviting_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "billing_account_member_invitation",
            },
        ),
    ]