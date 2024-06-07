from django.shortcuts import render, redirect

from sales_app.forms import mobileproduct_form
from sales_app.models import mobile_product, Seller, Pay


#
# def create_product(request):
#     data=mobileproduct_form()
#     if request.method=="POST":
#         data=mobileproduct_form(request.POST,request.FILES)
#         if data.is_valid():
#             data.save()
#             return redirect('product_table')
#     return render(request,'seller_dash/mobileproduct.html',{'formkey':data})


def create_product(request):
    current_user=request.user
    seller_object=Seller.objects.get(user=current_user)
    data=mobileproduct_form()
    if request.method=="POST":
        data=mobileproduct_form(request.POST,request.FILES)
        if data.is_valid():
            product= data.save(commit=False)
            product.seller = seller_object
            product.save()
            return redirect("product_table")
    return render(request,"seller_dash/mobileproduct.html",{'data':data})

def product_table(request):
    table = mobile_product.objects.all()
    return render(request,'seller_dash/productdetails.html',{'data':table})

def delete_product(request,id):
    data = mobile_product.objects.get(id=id)
    data.delete()
    return redirect("product_table")


def product_update(request,id):
    obj=mobile_product.objects.get(pk=id)
    data=mobileproduct_form(instance=obj)
    if request.method=="POST":
        data=mobileproduct_form(request.POST,request.FILES,instance=obj)
        if data.is_valid():
            data.save()
            return redirect('product_table')
    return render(request,"seller_dash/product_update.html",{"data":data})

def view_paid_cart(request):
    pay_objects = Pay.objects.filter(buy__cart__status = 1, buy__cart__product__seller__user = request.user )
    return render(request,"seller_dash/view_payments.html",{'pay_objects':pay_objects})
