from django.contrib import admin
from products.models import *
from order.models import *
from products.functions import *

class ImportMaterialAdmin(admin.ModelAdmin):
    model = ImportMaterial
    list_display= ('name', 'weight', 'cost_price', 'created_at') 
    list_filter = ('created_at',)
    search_fields = ('name__name',)
  
    

class ProductItemsAdmin (admin.TabularInline):
    model = ProductItem

class ProductCostAdmin (admin.TabularInline):
    model = ProductCost


class ProductAdmin (admin.ModelAdmin):
    inlines = [ProductItemsAdmin,ProductCostAdmin]
    list_display = ('name','is_available','cost_price', 'unit_price','discount' )
    list_filter = ('created_at','is_available')
    search_fields = ('name',)
    def cost_price(self, obj):
        cost = cost_price_product(obj.pk)
        return '{:,.0f}'.format(cost)
    cost_price.short_description = 'Giá thành'
         



def sold_weight(pk):
        cart_items = CartItems.objects.filter(product__productitem__name= pk)
        total_weight=0
        for item in cart_items:
            weight = item.qty*ProductItem.objects.filter(product = item.product, name=pk).first().weight
            total_weight = total_weight + weight
        return total_weight

class MaterialAdmin(admin.ModelAdmin):
    model= Material
    list_display = ('name','is_available','available_weight','sold_weight', 'str_import_weight', 'str_loss_weight')
    list_filter = ('created_at','is_available')
    search_fields = ('name',)
    def sold_weight(self, obj):
        weight = sold_weight(obj.pk)
        return '{:,.0f}'.format(weight)
    sold_weight.short_description = 'Khối lượng bán'
      
    def available_weight(self, obj):
        available =  obj.import_weight - obj.loss_weight - sold_weight(obj.pk)
        return '{:,.0f}'.format(available)
    available_weight.short_description = 'Khối lượng Khả dụng'

    def str_import_weight(self, obj):
        return '{:,.0f}'.format(obj.import_weight)
    str_import_weight.short_description = 'Khối lượng nhập'

    def str_loss_weight(self, obj):
        return '{:,.0f}'.format(obj.loss_weight)
    str_loss_weight.short_description = 'Khối lượng mất'

class MaterialLossAdmin(admin.ModelAdmin):
    models = MaterialLoss
    list_display = ('name', 'created_at','weight')
    list_filter = ('created_at',)
    search_fields = ('name__name',)
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ImportMaterial,  ImportMaterialAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(MaterialLoss, MaterialLossAdmin)
admin.site.register(Tag)