from django.contrib import admin
from .models import *
from order.models import Cart




class ClientAdmin (admin.ModelAdmin):
    model = Client
    list_display=('first_name', 'last_name', 'phone', 'total_value')
    field =['first_name', 'last_name', 'phone','address','birthday']
    search_fields = ('first_name', 'last_name', 'phone')
    readonly_fields= ['total_value']
    
    
    @admin.display(description='Tổng mua hàng')
    def total_value(self, obj):
        cart = Cart.objects.filter(client = obj.pk)
        total = sum(i.net_total_raw for i in cart)
        return f"{total:,}"
    

admin.site.register(Client, ClientAdmin)
