from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('go/order/', views.redirect_to_whatsapp, name='redirect_to_whatsapp'),  # 🔐 secure redirect
]