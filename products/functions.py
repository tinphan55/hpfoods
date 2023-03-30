from products.models import *
from order.models import *

def avg_cost(pk):
    last_import = ImportMaterial.objects.filter(name =pk).last()
    first_import = ImportMaterial.objects.filter(name =pk).first()
    start_time = first_import.created_at
    end_time = last_import.created_at
    import_w = sum(im.weight for im in ImportMaterial.objects.filter(name= pk,  created_at__gte=start_time, created_at__lt=end_time))
    loss_w = sum(loss.weight for loss in MaterialLoss.objects.filter(name= pk,  created_at__gte=start_time, created_at__lt=end_time))   
    cart_items = CartItems.objects.filter(product__productitem__name= pk,  created_at__gte=start_time, created_at__lt=end_time)
    sold_w=0
    for item in cart_items:
        weight = item.qty*ProductItem.objects.filter(product = item.product, name=pk).first().weight
        sold_w = sold_w + weight
    available =  import_w - loss_w - sold_w
    if import_w ==0:
        pre_cost = 0
    else:
        pre_cost = sum(im.weight*im.avg_cost for im in ImportMaterial.objects.filter(name= pk,  created_at__gte=start_time, created_at__lt=end_time))/import_w
    avg_cost = (pre_cost*available + last_import.weight*last_import.avg_cost)/(available+last_import.weight)
    return avg_cost

def cost_price_product(pk):
    meterial = ProductItem.objects.filter(product = pk)
    other_cost = ProductCost.objects.filter(product = pk)
    sum_cost = 0
    sum_orther_cost = 0
    for item in  meterial:
        cost = item.weight* avg_cost(item.name.pk)
        sum_cost = sum_cost + cost
    for i in other_cost:
        sum_orther_cost= i.cost + sum_orther_cost
    return round(sum_cost + sum_orther_cost ,0)