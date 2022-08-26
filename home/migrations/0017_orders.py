# Generated by Django 4.1 on 2022-08-26 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_order_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('address', models.TextField(default='')),
                ('city', models.TextField(default='')),
                ('state', models.TextField(default='')),
                ('zip', models.TextField(default='')),
                ('pro', models.TextField(default='')),
                ('sum', models.IntegerField(default=0)),
                ('status', models.TextField(default='ordered')),
                ('estimated_date', models.DateField(default=datetime.datetime(2022, 8, 26, 12, 14, 55, 77908))),
            ],
        ),
    ]
