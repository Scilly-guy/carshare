# Generated by Django 4.1.5 on 2023-01-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hardware", "0005_firmware_box_firmware_version_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="box",
            name="last_seen_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
