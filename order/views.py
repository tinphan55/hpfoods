
from order.models import *
from io import BytesIO
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Spacer
from django.template.loader import get_template
from reportlab.lib.units import cm
from django.template import loader
from django.http import HttpResponsePermanentRedirect
from hp_food import settings
from xhtml2pdf import pisa
import os




# def pdf(request, pk):
#     # Lấy dữ liệu cart theo pk truyền vào
#     cart = Cart.objects.get(pk=pk)
#     items = CartItems.objects.filter(cart=pk)
#     ship = CartTransport.objects.filter(cart=pk)
#     created_at = cart.created_at
#     client = cart.client

#     # Tạo template pdf từ HTML
#     template = get_template('bills/bill.html')
#     context = {
#         'created_at': created_at,
#         'client': client,
#         'items': items,
#         'cart': cart,
#         'ship': ship
#     }
#     html = template.render(context)

#     # Khởi tạo buffer để lưu trữ PDF
#     buffer = BytesIO()

#     # Tạo PDF
#     doc = SimpleDocTemplate(buffer, pagesize=A4)

#     # Tạo stylesheet
#     styles = getSampleStyleSheet()

#     # Thêm hình ảnh
#     logo = Image('http://hpfoods.vn/static/bills/img/logo.jpg')
#     logo.drawHeight = 2.5*cm
#     logo.drawWidth = 7.5*cm

#     # Thêm các paragraph từ HTML
#     elements = []
#     elements.append(logo)
#     elements.append(Spacer(1, 20))
#     for line in html.splitlines():
#         elements.append(Paragraph(line, styles["Normal"]))
#     doc.build(elements)
#     # Trả về file PDF cho client
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="bill.{pk}.pdf"'
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response




        

def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf to fetch additional resources such as
    stylesheets and images.
    """
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    else:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    return path



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
    html = template.render(context, request)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=bill.{pk}.pdf'
    buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer, link_callback=fetch_resources)
    #write PDF to file
    response.write(buffer.getvalue())
    buffer.close()
    return response


def redirect_view(request):
    return HttpResponsePermanentRedirect('https://shopee.vn/hpfoods?gidzl=7u7qR0_WPcGPdVLh1VvbPnALz6mOy3Cn3PltRaYjDpGDnlTl7ArcO0h7zJiQzpKm3vpnCJCaKw8v2k5kOW')