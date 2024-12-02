# Generated by Django 5.1.3 on 2024-11-29 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_image', models.ImageField(help_text='Upload the Dish image', upload_to='dishes/')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.restaurant')),
            ],
        ),
    ]