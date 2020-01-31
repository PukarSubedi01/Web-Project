from django.shortcuts import render, redirect
from application.forms.vendorsForm import vendorForm
from application.models.vendor import vendor
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication

@Authentication.valid_user
def vendors(request):
    vendors = vendor.objects.all()
    return render(request, "expense/vendor/vendors.html",{'vendors': vendors})

@Authentication.valid_user
def addvendor(request):
    if request.method == "POST":
        vendorsForm = vendorForm(request.POST)
        vendorsForm.save()
        return redirect("/vendors")
    vendorsForm = vendorForm()
    return render(request, "expense/vendor/newVendor.html", {'vendorsForm': vendorsForm})


@Authentication.valid_user
def edit_vendor(request,id):
    vendors = vendor.objects.get(id=id)
    return render(request,'expense/vendor/editVendor.html',{'vendors':vendors})

@Authentication.valid_user
def update_vendor(request,id):
    vendors=vendor.objects.get(id=id)
    form=vendorForm(request.POST,instance=vendors)
    form.save()
    return redirect('/vendors')

@Authentication.valid_user
def delete_vendor(request, id):
    vendor.objects.get(id=id)
    vendors = vendor.objects.get(id=id)
    vendors.delete()
    return redirect('/vendors')

