from django.shortcuts import render, redirect
from application.forms import userForm
from application.models import user


def signup(request):
    if request.method == "POST":
        usersForm = userForm(request.POST)
        if usersForm.is_valid():
            try:
                usersForm.save()
                return redirect()
            except:
                pass
    else:
        usersForm = userForm()
    return render(request, "signup.html", {'usersForm': usersForm})


def index(request):
    return render(request, "index.html")


def bills(request):
    return render(request, "bills.html")


def customers(request):
    return render(request, "customers.html")


def dashboard(request):
    return render(request, "Dashboard.html")


def invoices(request):
    return render(request, "invoices.html")


def items(request):
    return render(request, "items.html")


def vendors(request):
    return render(request, "vendors.html")


def newItem(request):
    return render(request, "NewItems.html")


def newBill(request):
    return render(request, "NewBills.html")


def newInvoice(request):
    return render(request, "NewInvoice.html")


def newCustomer(request):
    return render(request, "newCustomer.html")


def newVendor(request):
    return render(request, "newVendor.html")
