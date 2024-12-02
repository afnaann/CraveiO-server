# Generated by Django 5.1.3 on 2024-11-28 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('license_image', models.ImageField(help_text="Upload the shop's license image", upload_to='shop_licenses/')),
                ('latitude', models.DecimalField(decimal_places=6, help_text='Sorry, Restaurants Are Only From Kerala', max_digits=9, validators=[django.core.validators.MinValueValidator(8.18), django.core.validators.MaxValueValidator(12.48)])),
                ('longitude', models.DecimalField(decimal_places=6, help_text='Sorry, Restaurants Are Only From Kerala', max_digits=9, validators=[django.core.validators.MinValueValidator(74.7), django.core.validators.MaxValueValidator(77.3)])),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]