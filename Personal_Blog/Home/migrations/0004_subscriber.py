# Generated by Django 2.2.4 on 2019-10-29 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0003_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
    ]
