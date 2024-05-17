from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)


class Customer(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    place=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='seller')
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    qualification=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    place=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class mobile_product(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='mobile_product')
    name=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    description=models.TextField()
    image=models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cart_customer')
    product=models.ForeignKey(mobile_product,on_delete=models.CASCADE,related_name="cart_product")
    status=models.IntegerField(default=0)



class buy_now(models.Model):
    cart=models.ForeignKey(Cart,on_delete = models.CASCADE,related_name='cart_buy')
    phone=models.CharField(max_length = 10)
    adress=models.TextField()
    amount=models.CharField(max_length=100)


class Payment(models.Model):
    cart=models.ForeignKey(Cart,on_delete = models.CASCADE,related_name='cart')
    phone=models.CharField(max_length = 10)
    adress=models.TextField()
    card_number=models.CharField(max_length = 16)
    cvv=models.CharField(max_length = 3)
    expiry_date=models.CharField(max_length = 10)

