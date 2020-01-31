from django.shortcuts import redirect
from application.models.user import user

class Authentication:
    def valid_user(function):
        def wrap(request):
            try:
                user.objects.get(email=request.session['email'], password = request.session['password'])
                return function (request)
            except:
                return redirect('/index')
        return wrap