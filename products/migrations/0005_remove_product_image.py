# Generated by Django 3.1.6 on 2021-03-12 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210219_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
