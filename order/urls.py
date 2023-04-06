from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('bills/<int:pk>', views.billdetail, name='details'),
    path('', views.redirect_view),
    path('pdf/<int:pk>',views.pdf, name = 'pdf')
]