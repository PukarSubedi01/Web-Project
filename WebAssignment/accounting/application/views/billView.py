from django.shortcuts import render, redirect
from application.forms.billsForm import billForm
from application.models.bill import bill
from application.models.vendor import vendor
from django.http import HttpResponse, JsonResponse
from application.authenticate import Authentication


@Authentication.valid_user #authentication token
def bills(request):
    limit = 7
    page = 1
    if request.method == "POST":
        if "next" in request.POST:
            page = (int(request.POST['page']) + 1)
        elif "prev" in request.POST:
            page = (int(request.POST['page']) - 1)
        tempoffset = page - 1
        offset = tempoffset * limit
        bills = bill.objects.raw("select * from bill where user_id = %s limit 7 offset %s",
                                 [request.session['user_id'], offset]) #collecting data of currently logged in users
    else:
        bills = bill.objects.raw("select * from bill where user_id = %s limit 7 offset 0", [request.session['user_id']])
    return render(request, "expense/bill/bills.html", {'bills': bills, 'page': page})


@Authentication.valid_user
def newbill(request): #function to create a new bill
    vendors = vendor.objects.all()

    if request.method == "POST":
        if not request.POST._mutable:   #detecting if certain change is made to the data
            request.POST._mutable = True
        request.POST['user'] = request.session['user_id']
        billsForm = billForm(request.POST)
        billsForm.save()
        return redirect("/bills")
    else:
        billsForm = billForm()
    return render(request, "expense/bill/NewBills.html", {'billsForm': billsForm, 'vendors': vendors})


@Authentication.valid_user_include_id
def edit_bill(request, id): #function to edit bills
    vendors = vendor.objects.all()
    bills = bill.objects.get(id=id)
    return render(request, 'expense/bill/editBill.html', {'bills': bills, 'vendors': vendors})


@Authentication.valid_user_include_id
def update_bill(request, id):   #function to update bills
    bills = bill.objects.get(id=id)
    if not request.POST._mutable:   #detecting if certain change is made to the data
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form = billForm(request.POST, instance=bills)
    form.save()
    return redirect('/bills')


@Authentication.valid_user_include_id
def delete_bill(request, id):   #function to delete bills
    bill.objects.get(id=id)
    bills = bill.objects.get(id=id)
    bills.delete()
    return redirect('/bills')


@Authentication.valid_user
def searchBills(request):   #function to search bills
    bills = bill.objects.filter(id__icontains=request.GET['searchBills'],user_id=request.session['user_id']).values()
    return JsonResponse(list(bills), safe=False)
