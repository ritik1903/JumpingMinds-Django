# Generated by Django 4.1.7 on 2023-02-27 17:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lift", "0004_requests_per_lift"),
    ]

    operations = [
        migrations.RenameField(
            model_name="requests_per_lift",
            old_name="lift_id",
            new_name="lift",
        ),
    ]
