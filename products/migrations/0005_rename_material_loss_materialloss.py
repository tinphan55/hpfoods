# Generated by Django 4.1.5 on 2023-03-28 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Material_Loss',
            new_name='MaterialLoss',
        ),
    ]