from django.db import models


# Create your models here.
class Client (models.Model):
    first_name = models.CharField(max_length= 50,verbose_name = 'Họ')
    last_name = models.CharField(max_length= 50, verbose_name = 'Tên')
    phone = models.IntegerField(null=False, verbose_name = 'Điện thoại')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Ngày tạo')
    last_order_date = models.DateTimeField(auto_now=True, verbose_name = 'Ngày mua gần nhất')
    address = models.CharField(max_length=100, null= True, blank = True, verbose_name = 'Địa chỉ')
    birthday = models.DateField(null=True, blank = True, verbose_name = 'Ngày sinh')

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    class Meta:
        verbose_name = 'Khách hàng'
        verbose_name_plural = 'Khách hàng'
  