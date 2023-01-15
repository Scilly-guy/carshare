# Generated by Django 4.1.5 on 2023-01-15 22:05

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0007_boxaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boxaction",
            name="payload",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
            ),
        ),
        migrations.AlterModelTable(
            name="boxaction",
            table="box_action",
        ),
    ]
