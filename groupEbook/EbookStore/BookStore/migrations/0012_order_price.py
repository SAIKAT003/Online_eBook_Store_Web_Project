# Generated by Django 4.2.3 on 2023-08-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0011_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
