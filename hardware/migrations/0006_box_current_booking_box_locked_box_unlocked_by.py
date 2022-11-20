# Generated by Django 4.0.1 on 2022-04-13 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
        ("hardware", "0005_vehicle_operator_cards_etag_alter_vehicle_box"),
    ]

    operations = [
        migrations.AddField(
            model_name="box",
            name="current_booking",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bookings.booking",
            ),
        ),
        migrations.AddField(
            model_name="box",
            name="locked",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="box",
            name="unlocked_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="hardware.card",
            ),
        ),
    ]