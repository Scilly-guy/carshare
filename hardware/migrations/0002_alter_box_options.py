# Generated by Django 4.0 on 2022-01-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="box",
            options={"verbose_name_plural": "boxes"},
        ),
    ]
