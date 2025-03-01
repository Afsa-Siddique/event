# Generated by Django 5.1.3 on 2025-02-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('date_of_marriage', models.DateField()),
                ('number_of_participants', models.PositiveIntegerField()),
            ],
        ),
    ]
