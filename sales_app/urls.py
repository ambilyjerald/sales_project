from django.urls import path

from sales_app import views

urlpatterns = [
    path("",views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('loginpage',views.loginpage,name='loginpage')
]
