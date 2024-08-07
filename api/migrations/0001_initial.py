# Generated by Django 5.0.7 on 2024-08-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("property_name", models.CharField(max_length=255)),
                ("hotel_star_rating", models.CharField(max_length=255)),
                ("hotel_facilities", models.TextField()),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=255)),
                ("locality", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Place",
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
                ("zone", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("place_type", models.CharField(max_length=100)),
                ("establishment_year", models.CharField(max_length=50)),
                ("time_needed_to_visit", models.CharField(max_length=50)),
                ("google_review_rating", models.CharField(max_length=50)),
                ("entrance_fee", models.CharField(max_length=50)),
                ("airport_within_50km", models.CharField(max_length=100)),
                ("weekly_off", models.CharField(max_length=50)),
                ("significance", models.TextField()),
                ("dslr_allowed", models.CharField(max_length=50)),
                ("number_of_google_reviews", models.CharField(max_length=50)),
                ("best_time_to_visit", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("restaurant_name", models.CharField(max_length=255)),
                ("cuisine", models.CharField(max_length=255)),
                ("rating", models.FloatField()),
                ("average_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("area", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
            ],
        ),
    ]
