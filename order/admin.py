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
    list_display = ('image_tag','user','client', 'created_at', 'total','total_ship','net_total','title_with_link')
    fields = ('user','client','note', 'created_at')
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
    @admin.display(description='Tổng tiền hàng')
    def total(self, obj):
        return  obj.total
    @admin.display(description='Phí ship')
    def total_ship(self, obj):
         return  obj.total_ship
    @admin.display(description='Tổng thanh toán')
    def net_total(self, obj):
        return  obj.net_total
    
    # def pdf(self, obj):
    #     cart_item = obj.cartitems_set.first()
    #     if cart_item is None:
    #         return "None" 
    #     else:
    #         url = reverse('order:pdf', args=[obj.pk])
    #         return format_html("<a href='{}' target='_blank' style='background-color: #40a339; border-radius: 5px; color: white; padding: 5px;'>Tải pdf</a>", url)

    
class LossCartItemsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
         qs = super().get_queryset(request)
         return qs.filter(cart__is_loss=True)
    model= LossCartItems
    fields = ['product','qty','created_at','image','user', 'description' ]
    list_display = ['product','qty','created_at','image_tag','user' ]
    list_filter = ('created_at',)
    search_fields = ('product__name',)
    @admin.display(description='Hình ảnh')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<a href="{}" target="_blank"><img src="{}" width="100"/></a>'.format(obj.image.url, obj.image.url))
        else:
            return None
    



admin.site.register(Cart, CartAdmin)
admin.site.register(LossCartItems, LossCartItemsAdmin)