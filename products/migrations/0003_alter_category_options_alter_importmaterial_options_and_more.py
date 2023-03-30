# Generated by Django 4.1.5 on 2023-03-28 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_importmaterials_importmaterial_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Danh mục', 'verbose_name_plural': 'Danh mục'},
        ),
        migrations.AlterModelOptions(
            name='importmaterial',
            options={'verbose_name': 'Nhập nguyên liệu', 'verbose_name_plural': 'Nhập nguyên liệu'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Quản lý Nguyên liệu', 'verbose_name_plural': 'Quản lý Nguyên liệu'},
        ),
        migrations.AlterModelOptions(
            name='material_loss',
            options={'verbose_name': 'Hao hụt Nguyên liệu', 'verbose_name_plural': 'Hao hụt Nguyên liệu'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Sản phẩm', 'verbose_name_plural': 'Sản phẩm'},
        ),
        migrations.AddField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]