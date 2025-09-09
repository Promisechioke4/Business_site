from django import forms
from .models import OrderRequest

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['name', 'phone', 'product', 'note']
