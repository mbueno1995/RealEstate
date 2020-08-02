# Generated by Django 3.0.7 on 2020-06-17 15:18

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20200616_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custEmail', models.CharField(max_length=300)),
                ('custPassword', models.CharField(max_length=50)),
                ('custFname', models.CharField(max_length=200)),
                ('custLname', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=300)),
                ('custZipcode', models.CharField(max_length=50)),
                ('custPhone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
