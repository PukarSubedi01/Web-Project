from django.shortcuts import redirect
from application.models.user import user
from django.contrib import messages

class Authentication:
    def valid_user(function):
        def wrap(request):
            try:
                user.objects.get(email=request.session['email'], password = request.session['password'])
                return function (request)
            except:
                messages.warning(request,'The username/password you entered doesnot exist.Try again later!')
                return redirect('/index')
        return wrap

    def valid_user_include_id(function):
        def wrap(request,id):
            try:
                user.objects.get(email=request.session['email'], password = request.session['password'])
                return function (request,id)
            except:

                return redirect('/index')
        return wrap