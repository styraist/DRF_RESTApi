# Generated by Django 4.2.1 on 2023-05-09 17:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kitap",
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
                ("isim", models.CharField(max_length=255)),
                ("yazar", models.CharField(max_length=255)),
                ("aciklama", models.TextField(blank=True, null=True)),
                ("yaratilma_tarihi", models.DateTimeField(auto_now_add=True)),
                ("güncellenme_tarihi", models.DateTimeField(auto_now=True)),
                ("yayın_tarihi", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Yorum",
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
                ("yorum_sahibi", models.CharField(max_length=255)),
                ("yorum", models.TextField(blank=True, null=True)),
                ("yaratilma_tarihi", models.DateTimeField(auto_now_add=True)),
                ("güncellenme_tarihi", models.DateTimeField(auto_now=True)),
                (
                    "degerlendirme",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                (
                    "kitap",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="yorumlar",
                        to="kitaplar.kitap",
                    ),
                ),
            ],
        ),
    ]
