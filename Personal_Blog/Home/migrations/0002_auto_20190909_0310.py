# Generated by Django 2.2.4 on 2019-09-09 03:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 3, 10, 27, 215988, tzinfo=utc)),
        ),
    ]
