from django.shortcuts import render, redirect
from application.forms.itemsForm import itemForm
from application.models.items import items
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication


# @Authentication.valid_user
# def item(request):
#     item = items.objects.all();
#     return render(request, "items/items.html",{'item':item})

@Authentication.valid_user
def item(request):
    limit=7
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        item=items.objects.raw("select * from items where user_id = %s limit 7 offset %s",[request.session['user_id'], offset])
    else:
        item=items.objects.raw("select * from items where user_id = %s limit 7 offset 0",[request.session['user_id']])
    return render (request,"items/items.html",{'item':item, 'page': page})


@Authentication.valid_user
def newItem(request):
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user'] = request.session['user_id']
        itemsForm = itemForm(request.POST)
        itemsForm.save()
        return redirect("/items")
    itemsForm = itemForm()
    return render(request, "items/NewItems.html",{'itemsForm':itemsForm})

@Authentication.valid_user_include_id
def editItem(request,id):
    item = items.objects.get(id=id)
    return render(request,'items/editItems.html',{'item':item})

@Authentication.valid_user_include_id
def update_item(request,id):
    item=items.objects.get(id=id)
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form=itemForm(request.POST,instance=item)
    form.save()
    return redirect('/items')

@Authentication.valid_user_include_id
def delete_item(request, id):
    item = items.objects.get(id=id)
    item.delete()
    return redirect('/items')

@Authentication.valid_user
def searchItem(request):
    item = items.objects.filter(item_name__icontains = request.GET['searchItem']).values()
    return JsonResponse(list(item),safe=False)
