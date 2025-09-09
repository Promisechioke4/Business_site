from django.shortcuts import render, redirect
from .models import Video, SocialLink, Product
from django.utils.http import urlencode
from .forms import OrderForm
import os

# Create your views here.

from django.shortcuts import redirect
from urllib.parse import urlencode

def submit_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            message = f"Hi, my name is {order.name}. I want to order {order.product}."
            phone_number = "2349078218690"

            # Redirect to WhatsApp and back to show toast
            return redirect(f"https://wa.me/{phone_number}?{urlencode({'text': message})}#success")
    
    return redirect('/?success=true')  # fallback



def index(request):
    videos = Video.objects.filter(is_active=True)
    social_links = SocialLink.objects.all()
    products = Product.objects.filter(is_active=True)

    product_prefill = request.GET.get("product", "")
    form = OrderForm(initial={"product": product_prefill})

    return render(request, "index.html", {
        "videos": videos,
        "social_links": social_links,
        "form": form,
        "products": products,
    })


def redirect_to_whatsapp(request):
    product = request.GET.get('product', 'an item')
    phone_number = os.environ.get("WHATSAPP_NUMBER", "2349078218690")  # fallback
    message = f"Hi, I'm interested in ordering {product}"
    query = urlencode({"text": message})

    # This redirect happens server-side, number not in frontend
    return redirect(f"https://wa.me/{phone_number}?{query}")
