# coding: utf-8
from django import forms
from production.ping.models import PingProduct


class PingProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PingProductForm, self).__init__(*args, **kwargs)
        self.fields['product'].empty_label = "Select a product"
        self.fields['product'].empty_label = "Select a product"

    class Meta:
        model = PingProduct
