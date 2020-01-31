from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse





def index(request):
    return render(request, "index.html")



def dashboard(request):
    return render(request, "Dashboard.html")




def items(request):
    return render(request, "items.html")



def newItem(request):
    return render(request, "NewItems.html")







