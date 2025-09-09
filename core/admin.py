from django.contrib import admin
from .models import Video, SocialLink, OrderRequest, Product

# Register your models here.
admin.site.register(Video)
admin.site.register(SocialLink)
admin.site.register(Product)
@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'product', 'created_at')
    search_fields = ('name', 'phone', 'product')
    list_filter = ('created_at',)