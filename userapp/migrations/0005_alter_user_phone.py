# Generated by Django 5.1.3 on 2025-02-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
