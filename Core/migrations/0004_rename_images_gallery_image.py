# Generated by Django 4.2.4 on 2023-11-28 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Gallery_Image',
        ),
    ]