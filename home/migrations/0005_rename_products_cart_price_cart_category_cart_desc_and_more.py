# Generated by Django 4.1 on 2022-08-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.TextField(default='other'),
        ),
        migrations.AddField(
            model_name='cart',
            name='desc',
            field=models.TextField(default='h'),
        ),
        migrations.AddField(
            model_name='cart',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default='pt', max_length=50),
            preserve_default=False,
        ),
    ]