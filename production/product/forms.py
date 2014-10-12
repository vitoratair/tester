# coding: utf-8
from django import forms
from production.product.models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['typeProduct'].empty_label = "typeProduct"

    class Meta:
        model = Product
