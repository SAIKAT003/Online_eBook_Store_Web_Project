# Generated by Django 4.2.3 on 2023-08-26 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0007_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]