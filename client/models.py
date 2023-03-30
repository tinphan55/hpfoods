from django.db import models


# Create your models here.
class Client (models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    phone = models.IntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_order_date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100, null= True, blank = True)
    birthday = models.DateField(null=True, blank = True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    class Meta:
        verbose_name = 'Khách hàng'
        verbose_name_plural = 'Khách hàng'
  