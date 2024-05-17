from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from sales_app import views, admin_views, customer_views, seller_views

urlpatterns = [
    path("",views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('loginpage',views.loginpage,name='loginpage'),

    path('createcustomer',views.Create_customer,name='createcustomer'),
    path('createseller',views.Create_seller,name='createseller'),
    path('admindash',views.admindash,name='admindash'),
    path('customerdash',views.customerdash,name='customerdash'),
    path('sellerdash',views.sellerdash,name='sellerdash'),



    path('cus_read',admin_views.read_customer,name='cus_read'),
    path("cus_delete/<int:id>/",admin_views.delete_customer,name='cus_delete'),
    path("cus_update/<int:id>/",admin_views.update_customer,name='cus_update'),


    path('sel_read',admin_views.read_seller,name='sel_read'),
    path("sel_delete/<int:id>/",admin_views.delete_seller,name='sel_delete'),
    path("se_update/<int:id>/",admin_views.update_seller,name='sel_update'),


    path('cus_detail',customer_views.read_cus,name='cus_detail'),
    path("cus_del/<int:id>/",customer_views.del_customer,name='cus_del'),
    path("cus_up/<int:id>/",customer_views.up_customer,name='cus_up'),



    path('addproduct',seller_views.create_product,name='addproduct'),
    path("product_table",seller_views.product_table,name='product_table'),
    path("product_delete/<int:id>/",seller_views.delete_product,name="product_delete"),
    path("product_update/<int:id>/",seller_views.product_update,name="product_update"),


    path("admin_viewproducts",admin_views.admin_viewproducts,name='admin_viewproducts'),
    path("customer_viewproducts",customer_views.customer_viewproducts,name='customer_viewproducts'),

    path("add_to_cart/<int:id>/",customer_views.add_to_cart,name="add_to_cart"),
    path("view_cart/", customer_views.view_cart, name="view_cart"),
    path("delete_cart/<int:id>/", customer_views.delete_cart, name="delete_cart"),
    path("payment/<int:id>/", customer_views.payment, name="payment")










]
