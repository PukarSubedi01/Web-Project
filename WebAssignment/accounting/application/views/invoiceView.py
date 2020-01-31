from django.shortcuts import render, redirect
from application.forms.invoiceForm import invoiceForm
from application.models.invoice import invoice
from application.models.customer import customer
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication

@Authentication.valid_user
def invoices(request):
    invoices = invoice.objects.all()
    return render(request, "income/invoice/invoices.html",{'invoices': invoices})

@Authentication.valid_user
def newInvoice(request):
    customers = customer.objects.all()
    if request.method == "POST":
        invoicesForm = invoiceForm(request.POST)
        invoicesForm.save()
        return redirect("/invoices")
    else:
        invoicesForm = invoiceForm()
    return render(request, "income/invoice/NewInvoice.html",{'invoicesForm': invoicesForm,'customers':customers})

@Authentication.valid_user
def edit_invoice(request,id):
    customers = customer.objects.all()
    invoices = invoice.objects.get(id=id)
    return render(request,'income/invoice/editInvoice.html',{'invoices':invoices,'customers':customers})

@Authentication.valid_user
def update_invoice(request,id):
    invoices=invoice.objects.get(id=id)
    form=invoiceForm(request.POST,instance=invoices)
    form.save()
    return redirect('/invoices')

@Authentication.valid_user
def delete_invoice(request, id):
    invoice.objects.get(id=id)
    invoices = invoice.objects.get(id=id)
    invoices.delete()
    return redirect('/invoices')