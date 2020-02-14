from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from application.authenticate import Authentication
from application.models.bill import bill
from application.models.invoice import invoice
from application.models.user import user
from django.contrib import messages
from django.db.models import Q


def index(request):
    return render(request, "homepages/index.html")


def entry(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        u = user.objects.get(Q(email=request.POST['email']) & Q(password=request.POST['password']))
        request.session['user_id'] = u.id
        return redirect('/dashboard')
    except:
        messages.warning(request, "invalid username/password")
        return redirect('/index')


@Authentication.valid_user
def dashboard(request):
    expense = bill.objects.all()
    return render(request, "Dashboard.html", {'expense': expense})

@Authentication.valid_user
def getExpense(request):
    expense = bill.objects.filter(user_id=request.session['user_id']).values()
    return JsonResponse(list(expense), safe=False)

@Authentication.valid_user
def getIncome(request):
    income = invoice.objects.filter(user_id=request.session['user_id']).values()
    return JsonResponse(list(income), safe=False)


def logout(request):
    del request.session['email']
    del request.session['password']
    del request.session['user_id']
    return redirect('/index')
