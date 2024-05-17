from django.shortcuts import render, redirect

from sales_app.filters import product_filter_form
from sales_app.forms import sales_customer, sales_seller
from sales_app.models import Customer, Seller, mobile_product


def read_customer(request):
    data=Customer.objects.all()
    return render(request,'admin_dash/customerdetails.html',{'customerkey':data})

def delete_customer(request,id):
    data=Customer.objects.get(id=id)
    data.delete()
    return redirect('cus_read')

def update_customer(request,id):
    n=Customer.objects.get(id=id)
    form= sales_customer(instance=n)
    if request.method=="POST":
        form= sales_customer(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect("cus_read")
    return render(request,"admin_dash/customerupdate.html",{"form":form})


def read_seller(request):
    todo=Seller.objects.all()
    return render(request,'admin_dash/sellerdetails.html',{'todokey':todo})

def delete_seller(request,id):
    data=Seller.objects.get(id=id)
    data.delete()
    return redirect('sel_read')

# update method
def update_seller(request,id):
    n=Seller.objects.get(id=id)
    form= sales_seller(instance=n)
    if request.method=="POST":
        form= sales_seller(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect("sel_read")
    return render(request,"admin_dash/sellerupdate.html",{"form":form})

def admin_viewproducts(request):
    table = mobile_product.objects.all()
    searched_form = product_filter_form(request.GET,queryset=table)
    table=searched_form.qs
    context = {'table':table, 'searched_form':searched_form}
    return render(request,'admin_dash/products.html',context)

