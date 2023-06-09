# Generated by Django 4.1.5 on 2023-03-28 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit_price', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('discount', models.FloatField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='products.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('is_available', models.BooleanField(default=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.materials')),
            ],
        ),
        migrations.AddField(
            model_name='materials',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='products.tag'),
        ),
        migrations.CreateModel(
            name='Material_Loss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to='products.materials')),
            ],
        ),
        migrations.CreateModel(
            name='ImportMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('cost_price', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to='products.materials')),
            ],
        ),
    ]
