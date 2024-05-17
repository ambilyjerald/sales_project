from django.shortcuts import render, redirect

from sales_app.filters import product_filter_form
from sales_app.forms import sales_customer, payment_form
from sales_app.models import Customer, mobile_product, Cart


def read_cus(request):
    data=Customer.objects.all()
    return render(request,'customer_dash/customerdetails.html',{'customerkey':data})

def del_customer(request,id):
    data=Customer.objects.get(id=id)
    data.delete()
    return redirect('cus_read')

def up_customer(request,id):
    n=Customer.objects.get(id=id)
    form= sales_customer(instance=n)
    if request.method=="POST":
        form= sales_customer(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect("cus_read")
    return render(request,"customer_dash/customerupdate.html",{"form":form})

def customer_viewproducts(request):
    data = mobile_product.objects.all()
    searched_form = product_filter_form(request.GET,queryset=data)
    data=searched_form.qs
    context={'data':data,'searched_form':searched_form}
    return render(request,'customer_dash/productdetails.html',context)


def add_to_cart(request,id):
        customer_object=Customer.objects.get(user=request.user)
        product_object=mobile_product.objects.get(pk=id)
        cart_obj=Cart(customer=customer_object, product=product_object)
        cart_obj.save()
        return redirect('customer_viewproducts')


# get()-->Used when you expect to retrieve exactly one object.
# filter()-->Used when you expect to retrieve zero or more objects.

def view_cart(request):
    customer_object=Customer.objects.get(user=request.user)
    cart_objects=Cart.objects.filter(customer=customer_object)
    data=cart_objects
    return render(request,"customer_dash/view_cart.html",{'data':data})


def delete_cart(request,id):
    cart_object=Cart.objects.get(pk=id)
    cart_object.delete()
    return redirect("view_cart")

def payment(request,id):
    data = payment_form()
    if request.method == 'POST':
        data = payment_form(request.POST)
        if data.is_valid():
            payment_obj = data.save(commit=False)
            customer_obj = Customer.objects.get(user=request.user)
            cart_obj=Cart.objects.get(id=id)
            payment_obj.cart = cart_obj
            payment_obj.save()
            cart_obj.status = 1
            cart_obj.save()
            return redirect('view_cart')
    cart_object=Cart.objects.get(id=id)
    return render(request,'customer_dash/payment.html',{'data':data,'cart':cart_object})
