from django.shortcuts import render, redirect
from application.forms.usersForm import userForm
from application.models.user import user
from django.http import HttpResponse,JsonResponse
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        usersForm = userForm(request.POST)
        try:
            usersForm.save()
            messages.warning(request, "Registration successfull")
            return redirect('/index')

        except:
            request.session['email'] = request.POST['email']
            messages.warning(request, "The email you entered is already taken")
            return redirect('/signup')
    usersForm = userForm()
    return render(request, "homepages/signup.html", {'usersForm': usersForm})