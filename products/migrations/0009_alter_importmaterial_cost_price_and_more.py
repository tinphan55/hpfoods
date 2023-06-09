# Generated by Django 4.1.5 on 2023-03-31 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productcost_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importmaterial',
            name='cost_price',
            field=models.FloatField(verbose_name='Giá nhập'),
        ),
        migrations.AlterField(
            model_name='importmaterial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='importmaterial',
            name='description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='importmaterial',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa'),
        ),
        migrations.AlterField(
            model_name='importmaterial',
            name='name',
            field=models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to='products.material', verbose_name='Tên nguyên liệu'),
        ),
        migrations.AlterField(
            model_name='importmaterial',
            name='weight',
            field=models.FloatField(verbose_name='Khối lượng'),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='material',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Khả dụng'),
        ),
        migrations.AlterField(
            model_name='material',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nguyên liệu'),
        ),
        migrations.AlterField(
            model_name='materialloss',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='materialloss',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='materialloss',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa'),
        ),
        migrations.AlterField(
            model_name='materialloss',
            name='name',
            field=models.ForeignKey(limit_choices_to={'is_available': True}, on_delete=django.db.models.deletion.CASCADE, to='products.material', verbose_name='Tên nguyên liệu'),
        ),
        migrations.AlterField(
            model_name='materialloss',
            name='weight',
            field=models.FloatField(verbose_name='Khối lượng'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0, verbose_name='Giảm giá bán'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Khả dụng'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(verbose_name='Giá bán'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Tên'),
        ),
    ]
