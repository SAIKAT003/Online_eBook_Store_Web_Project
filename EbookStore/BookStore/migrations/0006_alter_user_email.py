# Generated by Django 4.2.3 on 2023-08-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0005_alter_books_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
