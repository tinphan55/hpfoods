# Generated by Django 4.1.5 on 2023-03-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcost',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
