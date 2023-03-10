# Generated by Django 4.1.4 on 2023-01-15 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bankapp", "0004_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicationform",
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
                ("name", models.CharField(max_length=100)),
                ("month", models.CharField(max_length=100)),
                ("day", models.CharField(max_length=100)),
                ("year", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=100)),
                ("age", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("account_type", models.CharField(max_length=100)),
                ("materials_provide", models.TextField()),
                (
                    "Branch_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bankapp.branch"
                    ),
                ),
                (
                    "District_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bankapp.district",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
