from django.shortcuts import render, redirect

from sales_app.filters import product_filter_form
from sales_app.forms import sales_customer, payment_form, customer_feedback_form
from sales_app.models import Customer, mobile_product, Cart, Buy_now, Feedback


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


def buy_now(request, cart_id):
    if request.method == 'POST':
        cart_object = Cart.objects.get(id = cart_id)
        cart = cart_object
        quantity = int(request.POST.get('quantity',0))
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        price = int(cart_object.product.price)
        amount = quantity*price
        buy_object = Buy_now(cart = cart,quantity = quantity,adress = adress,
        phone = phone,amount = amount)
        buy_object.save()
        current_object_id = buy_object.id
        return redirect("payment", buy_id = current_object_id)
    return render(request, "customer_dash/buy_now.html")



def payment(request, buy_id):
    data = payment_form()
    buy_object = Buy_now.objects.get(id = buy_id)
    print(buy_object)
    if request.method == 'POST':
        data = payment_form(request.POST)
        if data.is_valid():
            pay_object = data.save(commit = False)
            pay_object.buy=buy_object
            pay_object.save()
            cart_object = buy_object.cart
            cart_object.status = 1
            cart_object.save()
            return redirect('view_cart')
    return render(request, 'customer_dash/payment.html', {'data':data, 'buy_object':buy_object})


def customer_feed_back(request):
    feedback_form_data = customer_feedback_form()
    if request.method == 'POST':
        feedback_form_data = customer_feedback_form(request.POST)
        if feedback_form_data.is_valid():
            feedback_object = feedback_form_data.save(commit = False)
            feedback_object.customer = Customer.objects.get(user = request.user)

            feedback_object.save()
            return redirect('customerdash')
    return render(request, "customer_dash/customer_feed_back.html",{'feedback_form_data':feedback_form_data })

def customer_view_feedbacks(request):
    feedback_objects = Feedback.objects.filter(customer__user = request.user)
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer_dash/view_feedbacks.html",{'feedback_objects':feedback_objects})

def customer_delete_feedback(request, feedback_object_id):
    feedback_object = Feedback.objects.get(id = feedback_object_id)
    feedback_object.delete()
    return redirect('customer_view_feed_backs')
