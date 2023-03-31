from django.contrib import admin
from order.models import *
from django.urls import reverse
from django.utils.html import format_html
from django.utils.html import format_html_join
from member.models import *

class CartItemAdmin(admin.TabularInline):
    model = CartItems
    fields = ('product','qty','is_discount','discount', 'price','total_items')
    readonly_fields = ('price', 'discount','total_items')

class CartTransportAdmin(admin.StackedInline):
    model = CartTransport
    extra = 1



class CartAdmin(admin.ModelAdmin):
    inlines =[CartItemAdmin, CartTransportAdmin]
    model = Cart
    list_display = ('image_tag','user','client', 'created_at', 'total', 'total_discount','net_total','title_with_link')
    list_filter = ('created_at',)
    search_fields = ('client__phone',)
    list_display_links = ('client',)
    def title_with_link(self, obj):
        first_item = obj.cartitems_set.first()
        if first_item is None:
            return "None" 
        else:
            url = reverse('order:details', args=[obj.pk])
            return format_html("<a href='{}' target='_blank' style='background-color: #007bff; border-radius: 5px; color: white; padding: 5px;'>Click xem bill</a>", url)
    title_with_link.short_description = 'Hóa đơn'

    def image_tag(self, obj):
        member = Member.objects.filter(id_member_id =obj.user_id).first()
        if member is not None and member.avatar:
            return format_html('<img src="{}" style="border-radius: 50%; width: 40px; height: 40px; object-fit: cover;"/>'.format(member.avatar.url))
        else:
            return format_html('<img src="/media/member/default-image.jpg"style="border-radius: 50%; width: 40px; height: 40px; object-fit: cover;"/>')                   

    image_tag.short_description = 'avatar'
    @admin.display(description='Tổng tiền trước giảm')
    def total(self, obj):
        return  obj.total
    @admin.display(description='Tổng giảm giá')
    def total_discount(self, obj):
        return  obj.total_discount
    @admin.display(description='Tổng thanh toán')
    def net_total(self, obj):
        return  obj.net_total
   
# Register your models here.
admin.site.register(Cart, CartAdmin)