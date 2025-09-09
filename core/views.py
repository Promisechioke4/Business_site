from urllib.parse import urlencode
from django.shortcuts import render, redirect
from .models import Video, SocialLink, Product
from .forms import OrderForm
from django.urls import reverse
import os

def submit_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            # Direct access to the related Product object
            product = order.product

            try:
                image_url = request.build_absolute_uri(product.image.url)
            except:
                image_url = "Image not available"

            message = (
                f"Hi, I want to order *{product.name}*.🛒\n\n"
                f"📸 Product Image: {image_url}\n\n"
                f"📞 Phone: {order.phone}\n"
                f"🧍 Name: {order.name}\n"
                f"📝 Note: {order.note if order.note else 'N/A'}"
            )

            params = urlencode({
                'whatsapp': 'true',
                'message': message
            })

            return redirect(f"{reverse('index')}?{params}")

    return redirect(reverse('index'))




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
    phone_number = os.environ.get("WHATSAPP_NUMBER", "+2348147726414")  # fallback
    message = f"Hi, I'm interested in ordering {product}"
    query = urlencode({"text": message})

    # This redirect happens server-side, number not in frontend
    return redirect(f"https://wa.me/{phone_number}?{query}")
