from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import generic


class LoginView(generic.View):

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('blog:index')

        return render(request, 'loginsys/login.html')



