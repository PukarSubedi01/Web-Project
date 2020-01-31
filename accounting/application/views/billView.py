from django.shortcuts import render, redirect
from application.forms.billsForm import billForm
from application.models.bill import bill
from application.models.vendor import vendor
from django.http import HttpResponse,JsonResponse

def bills(request):
    bills = bill.objects.all()
    return render(request, "expense/bill/bills.html",{'bills':bills})

def newbill(request):
    vendors=vendor.objects.all()
    if request.method == "POST":
        billsForm = billForm(request.POST)
        billsForm.save()
        return redirect("/bills")
    else:
        billsForm = billForm()
    return render(request, "expense/bill/NewBills.html", {'billsForm': billsForm,'vendors':vendors})

def edit_bill(request,id):
    vendors = vendor.objects.all()
    bills = bill.objects.get(id=id)
    return render(request,'expense/bill/editBill.html',{'bills':bills,'vendors':vendors})

def update_bill(request,id):
    bills=bill.objects.get(id=id)
    form=billForm(request.POST,instance=bills)
    form.save()
    return redirect('/bills')


def delete_bill(request, id):
    bill.objects.get(id=id)
    bills = bill.objects.get(id=id)
    bills.delete()
    return redirect('/bills')
