# Generated by Django 4.1 on 2022-08-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_orders_estimated_date_delete_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]