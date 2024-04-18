from django.urls import path

from sales_app import views

urlpatterns = [
    path("",views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('loginpage',views.loginpage,name='loginpage'),
    # path('createlogin',views.Create_login,name='createlogin'),
    path('createcustomer',views.Create_customer,name='createcustomer'),
    path('createseller',views.Create_seller,name='createseller')
]
