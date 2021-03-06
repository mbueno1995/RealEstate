# Generated by Django 3.0.7 on 2020-06-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20200611_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='bedrooms',
            new_name='BDS',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bathrooms',
        ),
        migrations.AddField(
            model_name='property',
            name='BA',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
