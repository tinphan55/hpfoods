from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from order.models import *



def billdetail(request, pk):
    template = loader.get_template('bills/bill.html')
    cart = Cart.objects.get(pk=pk)
    items = CartItems.objects.filter(cart = pk)
    ship = CartTransport.objects.filter(cart = pk)
    context = {
        'created_at':cart.created_at,
        'client': cart.client,
        'items':items,
        'cart':cart,
        'ship':ship

    }
    return HttpResponse(template.render(context, request))

def pdf(request, pk):
    bills = Bill.objects.get(pk=pk)
    template = loader.get_template('bills/bill2.html')
    context = context_bill(pk)
    html = template.render(context, request)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=bill_{pk}.pdf'
    pisa.CreatePDF(html, dest=response, link_callback=fetch_resources)
    return response