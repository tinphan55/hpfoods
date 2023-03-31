from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from client.models import *
from products.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    note = models.TextField(max_length=500, null= True, blank=True)
 
    class Meta:
        verbose_name = 'Đơn hàng'
        verbose_name_plural = 'Đơn hàng'

    def __str__(self):
        return str(self.id) + '_' + str(self.client) 
    
    def return_id_cart(self):
        return self.id
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
    def net_total_raw (self):
        return self.total_raw -self.total_discount_raw
    
    @property
    def net_total(self):
        return  '{:,.0f}'.format(self.net_total_raw)
    

    

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(default=datetime.now)
    price = models.FloatField(blank=True, default=0)
    qty = models.IntegerField(default=1)
    discount = models.IntegerField(null= True, blank=True, default=0)
    is_discount = models.BooleanField(default=False)  
    total_items = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Mua hàng'
        verbose_name_plural = 'Mua hàng'
    
    
    def save(self, *args, **kwargs):
        self.price = self.product.unit_price
        self.total_items = self.price*self.qty
        if self.is_discount == True:
            self.discount = self.product.discount* self.qty
        else:
            self.discount = 0
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
        total_items = self.total_items - self.discount
        return '{:,.0f}'.format( total_items)
