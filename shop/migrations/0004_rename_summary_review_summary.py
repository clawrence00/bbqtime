# Generated by Django 3.2.21 on 2023-09-30 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Summary',
            new_name='summary',
        ),
    ]
