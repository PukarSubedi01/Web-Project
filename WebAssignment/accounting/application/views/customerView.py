from django.shortcuts import render, redirect
from application.forms.customersForm import customerForm
from application.models.customer import customer
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication


@Authentication.valid_user
def customers(request):
    limit=7
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        customers=customer.objects.raw("select * from customer where user_id = %s limit 7 offset %s",[request.session['user_id'],offset])
    else:
        customers=customer.objects.raw("select * from customer where user_id = %s limit 7 offset 0",[request.session['user_id']])
    return render (request,"income/customer/customers.html",{'customers':customers, 'page': page})

@Authentication.valid_user
def addcustomer(request):
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user'] = request.session['user_id']
        customersForm = customerForm(request.POST)
        customersForm.save()
        return redirect("/customers")
    customersForm = customerForm()
    return render(request, "income/customer/newCustomer.html", {'customersForm': customersForm})

@Authentication.valid_user_include_id
def editCustomers(request,id):
    customers = customer.objects.get(id=id)
    return render(request,'income/customer/editCustomer.html',{'customers':customers})

@Authentication.valid_user_include_id
def update_customer(request,id):
    customers=customer.objects.get(id=id)
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form=customerForm(request.POST,instance=customers)
    form.save()
    return redirect('/customers')

@Authentication.valid_user_include_id
def delete_customer(request, id):
    customer.objects.get(id=id)
    customers = customer.objects.get(id=id)
    customers.delete()
    return redirect('/customers')

@Authentication.valid_user
def searchCustomers(request):
    customers = customer.objects.filter(name__icontains=request.GET['searchCustomers']).values()
    return JsonResponse(list(customers), safe=False)

