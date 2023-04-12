from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from client.models import *
from products.models import Product
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied



# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, 
         verbose_name='Người tạo')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Khách hàng')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Ngày tạo')
    note = models.TextField(max_length=500, null= True, blank=True, verbose_name='Ghi chú')
    is_loss = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Đơn hàng'
        verbose_name_plural = 'Đơn hàng'

    def __str__(self):
        return str(self.id) + '_' + str(self.client) 
    
    def return_id_cart(self):
        return self.id
    
    # tổng bao gồm có giảm giá
    @property
    def total_raw (self):
        items= CartItems.objects.filter(cart = self.pk)
        total = sum(i.total_items for i in items)
        return total
    @property
    def total(self):
        return  '{:,.0f}'.format(self.total_raw)
    
    @property
    def total_discount_raw (self):
        items= CartItems.objects.filter(cart = self.pk)
        total = sum(i.discount for i in items)
        return total
    @property
    def total_discount(self):
        return  '{:,.0f}'.format(self.total_discount_raw)
    
    @property
    def total_ship_raw (self):
        ship= CartTransport.objects.filter(cart = self.pk)
        return sum(j.cost for j in ship)
    @property
    def total_ship(self):
        return  '{:,.0f}'.format(self.total_ship_raw)
    

    # tổng cần thu, gồm cả phí ship 
    @property
    def net_total_raw (self):
        return self.total_raw + self.total_ship_raw
    
    @property
    def net_total(self):
        return  '{:,.0f}'.format(self.net_total_raw)
    
@receiver(pre_delete, sender= Cart)
def prevent_delete(sender, instance, **kwargs):
    if instance.id == 41:
        raise PermissionDenied("Cart mặc định, không được xóa")
    

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                verbose_name='Sản phẩm')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)  
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Ngày tạo')
    price = models.FloatField(blank=True, default=0, verbose_name='Giá bán')
    qty = models.IntegerField(default=1, verbose_name='Số lượng')
    discount = models.IntegerField(null= True, blank=True, default=0, verbose_name='Giảm giá')
    is_discount = models.BooleanField(default=False,
        help_text="Nếu có giảm giá chọn", verbose_name='Có giảm giá')  
    image = models.ImageField(upload_to='order/loss', null = True, blank=True)
    description = models.TextField(max_length=500, null= True, blank=True, verbose_name='Mô tả')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null= True, blank=True,
         verbose_name='Người tạo')
    total_items = models.IntegerField(default=0, verbose_name='Tổng giá')
    
    class Meta:
        verbose_name = 'Mua hàng'
        verbose_name_plural = 'Mua hàng'
    def __str__(self):
        return str(self.product) 
    
    
    def save(self, *args, **kwargs):
        if self.is_discount == True:
            self.discount = self.product.discount
            
        else:
            self.discount = 0
        self.price = self.product.unit_price - self.discount
        self.total_items = self.price*self.qty 
        super(CartItems, self).save(*args, **kwargs)
    

    @property
    def str_price(self):
        price = self.price
        return '{:,.0f}'.format(price)
    @property
    def str_qty(self):
        qty = self.qty
        return '{:,.0f}'.format(qty)
    @property
    def str_discount(self):
        discount = self.discount
        return '{:,.0f}'.format( discount)
    @property
    def str_total_items(self):
        total_items = self.total_items 
        return '{:,.0f}'.format( total_items)

class CartTransport(models.Model):
    PARTNER_CHOICES = (
        ('Viettel', 'Viettel'),
        ('Giao hàng nhanh', 'Giao hàng nhanh'),
        ('Giao hàng tiết kiệm', 'Giao hàng tiết kiệm'),
        ('HPfoods', 'HPfoods'),
        ('Khác', 'Khác'),
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  
    partner = models.CharField(max_length=50, choices=PARTNER_CHOICES, 
             default='hbfoods',  verbose_name = 'Đơn vị giao hàng')
    cost = models.FloatField(default=0, verbose_name = 'Chi phí')
    note = models.TextField(max_length=500, null= True, blank=True, verbose_name='Ghi chú')
    class Meta:
        verbose_name = 'Giao hàng'
        verbose_name_plural = 'Giao hàng'
    def __str__(self):
        return str(self.partner) 

    @property
    def str_cost(self):
        price = self.cost
        return '{:,.0f}'.format(price)

class LossCartItems (CartItems):
    class Meta:
        proxy = True
        verbose_name = 'Hao hụt hàng hóa'
        verbose_name_plural = 'Hao hụt hàng hóa'
    def __str__(self):
        return str(self.product)
        
    def save(self, *args, **kwargs):
        self.total_items = 0
        self.cart_id = 41
        super(LossCartItems, self).save(*args, **kwargs)