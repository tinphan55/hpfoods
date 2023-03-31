# Generated by Django 4.1.5 on 2023-03-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Khách hàng', 'verbose_name_plural': 'Khách hàng'},
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Ngày sinh'),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Họ'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_order_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày mua gần nhất'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(verbose_name='Điện thoại'),
        ),
    ]
