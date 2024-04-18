from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)


class Customer(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='customer')
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Phone=models.CharField(max_length=20)
    Email=models.EmailField()
    Place=models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Seller(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='seller')
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Qualification=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Email=models.EmailField()
    Place=models.CharField(max_length=50)

    def __str__(self):
        return self.Name



