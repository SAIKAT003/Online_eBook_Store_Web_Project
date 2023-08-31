# Generated by Django 4.2.4 on 2023-08-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0002_alter_books_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]