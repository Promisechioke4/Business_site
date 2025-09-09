from django import forms
from .models import OrderRequest, Product

class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label="Select a product"
    )

    class Meta:
        model = OrderRequest
        fields = ['name', 'phone', 'product']
