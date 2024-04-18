from django.shortcuts import render, redirect

from sales_app.forms import sales_login, sales_customer, sales_seller


# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def loginpage(request):
    return render(request,'login.html')

def Create_customer(request):
    form1=sales_login()
    form2=sales_customer()
    if request.method=='POST':
        obj1=sales_login(request.POST)
        obj2=sales_customer(request.POST)
        if obj1.is_valid() and obj2.is_valid():
            a=obj1.save(commit=False)
            a.is_customer=True
            a.save()
            user1=obj2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect("/")

    return render(request,'Registration.html',{'formkey1':form1,'formkey2':form2})


def Create_seller(request):
    form1=sales_login()
    form2=sales_seller()
    if request.method=='POST':
        obj1=sales_login(request.POST)
        obj2=sales_seller(request.POST)
        if obj1.is_valid() and obj2.is_valid():
            a=obj1.save(commit=False)
            a.is_seller=True
            a.save()
            user1=obj2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect("/")

    return render(request,'Registration.html',{'formkey1':form1,'formkey2':form2})



