# Generated by Django 4.1.5 on 2023-03-28 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImportMaterials',
            new_name='ImportMaterial',
        ),
        migrations.RenameModel(
            old_name='Materials',
            new_name='Material',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='ProductItems',
            new_name='ProductItem',
        ),
    ]