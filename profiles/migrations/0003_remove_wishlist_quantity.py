# Generated by Django 3.2.21 on 2023-10-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='quantity',
        ),
    ]
