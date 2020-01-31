from django.shortcuts import render, redirect
from application.forms.usersForm import userForm
from application.models.user import user
from django.http import HttpResponse,JsonResponse

def signup(request):
    if request.method == "POST":
        usersForm = userForm(request.POST)
        usersForm.save()
        return redirect()
    usersForm = userForm()
    return render(request, "signup.html", {'usersForm': usersForm})