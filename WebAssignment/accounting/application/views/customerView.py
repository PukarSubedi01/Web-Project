from django.shortcuts import render, redirect
from application.forms.customersForm import customerForm
from application.models.customer import customer
from django.http import HttpResponse,JsonResponse

def customers(request):
    customers = customer.objects.all()
    return render(request, "income/customer/customers.html",{'customers':customers})

def addcustomer(request):
    if request.method == "POST":
        customersForm = customerForm(request.POST)
        customersForm.save()
        return redirect("/customers")
    customersForm = customerForm()
    return render(request, "income/customer/newCustomer.html", {'customersForm': customersForm})

def editCustomers(request,id):
    customers = customer.objects.get(id=id)
    return render(request,'income/customer/editCustomer.html',{'customers':customers})

def update_customer(request,id):
    customers=customer.objects.get(id=id)
    form=customerForm(request.POST,instance=customers)
    form.save()
    return redirect('/customers')

def delete_customer(request, id):
    customer.objects.get(id=id)
    customers = customer.objects.get(id=id)
    customers.delete()
    return redirect('/customers')
