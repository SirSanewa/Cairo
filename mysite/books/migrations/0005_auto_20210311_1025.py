# Generated by Django 3.1.7 on 2021-03-11 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210311_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='ratings_amount',
            field=models.IntegerField(default=0),
        ),
    ]
