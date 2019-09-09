# Generated by Django 2.2.4 on 2019-09-09 03:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('paragraph', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 9, 9, 3, 16, 44, 404634, tzinfo=utc))),
            ],
        ),
    ]
