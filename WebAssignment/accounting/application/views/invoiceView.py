from django.shortcuts import render, redirect
from application.forms.invoiceForm import invoiceForm
from application.models.invoice import invoice
from application.models.customer import customer
from django.http import HttpResponse, JsonResponse
from application.authenticate import Authentication

@Authentication.valid_user
def invoices(request):
    limit=7
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        invoices=invoice.objects.raw("select * from invoice where user_id=%s limit 7 offset %s",
                                 [request.session['user_id'], offset])
    else:
        invoices=invoice.objects.raw("select * from invoice where user_id = %s limit 7 offset 0",[request.session['user_id']])
    return render (request,"income/invoice/invoices.html",{'invoices':invoices, 'page': page})



@Authentication.valid_user
def newInvoice(request):
    customers = customer.objects.all()
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user'] = request.session['user_id']
        invoicesForm = invoiceForm(request.POST)
        invoicesForm.save()
        return redirect("/invoices")
    else:
        invoicesForm = invoiceForm()
    return render(request, "income/invoice/NewInvoice.html", {'invoicesForm': invoicesForm, 'customers': customers})


@Authentication.valid_user_include_id
def edit_invoice(request, id):
    customers = customer.objects.all()
    invoices = invoice.objects.get(id=id)
    return render(request, 'income/invoice/editInvoice.html', {'invoices': invoices, 'customers': customers})


@Authentication.valid_user_include_id
def update_invoice(request, id):
    invoices = invoice.objects.get(id=id)
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form = invoiceForm(request.POST, instance=invoices)
    form.save()
    return redirect('/invoices')


@Authentication.valid_user_include_id
def delete_invoice(request, id):
    invoice.objects.get(id=id)
    invoices = invoice.objects.get(id=id)
    invoices.delete()
    return redirect('/invoices')


@Authentication.valid_user
def searchInv(request):
    invoices = invoice.objects.filter(id__icontains=request.GET['searchInv']).values()
    return JsonResponse(list(invoices), safe=False)
