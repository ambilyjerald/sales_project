import django_filters
from django_filters import FilterSet, CharFilter

from django import forms
from .models import mobile_product, Pay


class product_filter_form(FilterSet):
    brand=CharFilter(lookup_expr='icontains',widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'search by brand'}))
    seller_name= CharFilter(field_name='seller__name',lookup_expr='icontains', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'search by seller name'}))

    class Meta:
        model = mobile_product
        fields = ['brand','seller_name']

class pay_filter_form(FilterSet):
    seller_name = CharFilter(field_name = 'buy__cart__product__seller__name',lookup_expr = 'icontains',
         widget = forms.TextInput(attrs={'placeholder':'Search by seller name'}))
    class Meta:
        model = Pay
        fields = ['seller_name',]
