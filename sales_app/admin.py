from django.contrib import admin
from sales_app import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Customer)
admin.site.register(models.Seller)
admin.site.register(models.mobile_product)
admin.site.register(models.Cart)
admin.site.register(models.Buy_now)
admin.site.register(models.Pay)
admin.site.register(models.Feedback)

