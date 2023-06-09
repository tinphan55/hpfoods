# Generated by Django 4.1.5 on 2023-03-31 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_carttransport_alter_cart_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carttransport',
            options={'verbose_name': 'Giao hàng', 'verbose_name_plural': 'Giao hàng'},
        ),
        migrations.AddField(
            model_name='carttransport',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carttransport',
            name='partner',
            field=models.CharField(choices=[('Viettel', 'Viettel'), ('ghn', 'Giao hàng nhanh'), ('ghtk', 'Giao hàng tiết kiệm'), ('hbfoods', 'HPfoods'), ('other', 'Khác')], default='hbfoods', max_length=50, verbose_name='Đơn vị giao hàng'),
        ),
    ]
