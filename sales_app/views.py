from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from sales_app.forms import sales_login, sales_customer, sales_seller


# Create your views here.
def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindash')
            elif user.is_customer:
                return redirect('customerdash')
            elif user.is_seller:
                return redirect('sellerdash')

        else:
            messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')


def Create_customer(request):
    form1 = sales_login()
    form2 = sales_customer()
    if request.method == 'POST':
        form1 = sales_login(request.POST)
        form2 = sales_customer(request.POST)
        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("/")

    return render(request, 'Registration.html', {'formkey1': form1, 'formkey2': form2})


def Create_seller(request):
    form1 = sales_login()
    form2 = sales_seller()
    if request.method == 'POST':
        form1 = sales_login(request.POST)
        form2 = sales_seller(request.POST)
        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_seller = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("/")

    return render(request, 'Registration.html', {'formkey1': form1, 'formkey2': form2})


def admindash(request):
    return render(request, 'admin_dash/admindashboard.html')


def customerdash(request):
    return render(request, 'customer_dash/customerdashboard.html')


def sellerdash(request):
    return render(request, 'seller_dash/sellerdashboard.html')





