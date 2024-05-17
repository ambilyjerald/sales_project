from django.contrib.auth.forms import UserCreationForm
from django import forms

from sales_app.models import Login_view, Customer, Seller, mobile_product, Payment


class sales_login(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=Login_view
        fields=('username','password1','password2')


class sales_customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('__all__')
        exclude=('user','status1')


class sales_seller(forms.ModelForm):
    class Meta:
        model=Seller
        fields=('__all__')
        exclude=('user','status2')

class mobileproduct_form(forms.ModelForm):
    class Meta:
        model = mobile_product
        fields=('__all__')
        exclude=('seller',)


class dateinput(forms.DateInput):
    input_type = 'date'


class payment_form(forms.ModelForm):
     date=forms.DateField(widget=dateinput())
     class Meta:
        model = Payment
        fields = ('__all__')
        exclude = ('cart',)
        # for single field in exclude comma(,) is needed
