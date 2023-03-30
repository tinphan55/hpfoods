from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    id_member= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='member', null = True, blank=True,default = "")

    def __str__(self):
        return super().__str__()
    class Meta:
        verbose_name = 'More'
        verbose_name_plural = 'More'