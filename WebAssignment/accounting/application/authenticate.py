from django.shortcuts import redirect
from application.models.user import user
from django.contrib import messages

#class where authentication is done
class Authentication:
    def valid_user(function):
        def wrap(request):
            try:
                user.objects.get(email=request.session['email'], password = request.session['password'])
                return function (request)
            except:
                messages.warning(request,'Please login first')
                return redirect('/index')
        return wrap

    def valid_user_include_id(function): #function for authentication when id is present
        def wrap(request,id):
            try:
                user.objects.get(email=request.session['email'], password = request.session['password'])
                return function (request,id)
            except:

                return redirect('/index')
        return wrap