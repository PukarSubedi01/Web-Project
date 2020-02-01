from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from application.authenticate import Authentication




def index(request):
    return render(request, "index.html")

def entry(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/dashboard')

@Authentication.valid_user
def dashboard(request):
    return render(request, "Dashboard.html")



@Authentication.valid_user
def items(request):
    return render(request, "items/items.html")


@Authentication.valid_user
def newItem(request):
    return render(request, "items/NewItems.html")







