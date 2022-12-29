# Generated by Django 4.1.3 on 2022-12-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0002_initial"),
        ("bookings", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="billing_account",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bookings",
                to="billing.billingaccount",
            ),
            preserve_default=False,
        ),
    ]
