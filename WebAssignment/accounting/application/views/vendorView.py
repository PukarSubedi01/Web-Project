from django.shortcuts import render, redirect
from application.forms.vendorsForm import vendorForm
from application.models.vendor import vendor
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication

@Authentication.valid_user
def vendors(request):
    limit=7
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        vendors=vendor.objects.raw("select * from vendor where user_id = %s  limit 7 offset %s",[request.session['user_id'],offset])
    else:
        vendors=vendor.objects.raw("select * from vendor where user_id = %s  limit 7 offset 0",[request.session['user_id']])
    return render (request,"expense/vendor/vendors.html",{'vendors':vendors, 'page': page})

@Authentication.valid_user
def addvendor(request):
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user'] = request.session['user_id']
        vendorsForm = vendorForm(request.POST)
        vendorsForm.save()
        return redirect("/vendors")
    vendorsForm = vendorForm()
    return render(request, "expense/vendor/newVendor.html", {'vendorsForm': vendorsForm})


@Authentication.valid_user_include_id
def edit_vendor(request,id):
    vendors = vendor.objects.get(id=id)
    return render(request,'expense/vendor/editVendor.html',{'vendors':vendors})

@Authentication.valid_user_include_id
def update_vendor(request,id):
    vendors=vendor.objects.get(id=id)
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form=vendorForm(request.POST,instance=vendors)
    form.save()
    return redirect('/vendors')

@Authentication.valid_user_include_id
def delete_vendor(request, id):
    vendor.objects.get(id=id)
    vendors = vendor.objects.get(id=id)
    vendors.delete()
    return redirect('/vendors')

@Authentication.valid_user
def searchVendors(request):
    vendors = vendor.objects.filter(name__icontains=request.GET['searchVendors']).values()
    return JsonResponse(list(vendors), safe=False)

