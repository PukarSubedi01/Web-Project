from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from application.authenticate import Authentication
from application.models.bill import bill
from application.models.user import user
from django.db.models import Q


def index(request):
    return render(request, "homepages/index.html")


def entry(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        u = user.objects.get(Q(email=request.POST['email']) & Q(password=request.POST['password']))
        request.session['user_id']=u.id
        return redirect('/dashboard')
    except:
        return redirect('/index')



@Authentication.valid_user
def dashboard(request):
    expense = bill.objects.raw("select total from bill")
    return render(request, "Dashboard.html", {'expense': expense})


def logout(request):
    del request.session['email']
    del request.session['passwords']
    return redirect('/index')
