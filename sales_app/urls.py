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
    path("buy_now/<int:cart_id>/", customer_views.buy_now, name="buy_now"),
    path("delete_cart/<int:id>/", customer_views.delete_cart, name="delete_cart"),
    path("payment/<int:buy_id>/", customer_views.payment, name="payment"),
    path("view_view_paid_cart/", seller_views.view_paid_cart, name = "view_paid_cart"),

    path("customer_feed_back/", customer_views.customer_feed_back, name="customer_feed_back"),
    path("customer_view_feedbacks/", customer_views.customer_view_feedbacks, name="customer_view_feed_backs"),
    path("admin_view_feedbacks/", admin_views.admin_view_feedbacks, name="admin_view_feed_backs"),
    path("admin_view_orders", admin_views.admin_view_orders, name="admin_view_orders"),
    path("admin_update_reply/<int:feedback_object_id>", admin_views.admin_update_reply, name="admin_update_reply"),
    path("customer_delete_feedback/<int:feedback_object_id>/", customer_views.customer_delete_feedback, name="customer_delete_feedback"),
    path("logout/", views.logout_view, name="logout_view")











]
