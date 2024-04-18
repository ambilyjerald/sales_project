from django.contrib.auth.forms import UserCreationForm
from django import forms

from sales_app.models import Login_view, Customer, Seller



class sales_login(UserCreationForm):
    UserName=forms.CharField()
    Password1=forms.CharField(label='password',widget=forms.PasswordInput)
    Password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=Login_view
        fields=('UserName','Password1','password2')


class sales_customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('__all__')
        exclude=('user','status1','PASSWORD','PASSWORD CONFIRMATION')


class sales_seller(forms.ModelForm):
    class Meta:
        model=Seller
        fields=('__all__')
        exclude=('user','status2','PASSWORD','PASSWORD CONFIRMATION')





