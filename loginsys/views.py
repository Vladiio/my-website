from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import generic
from loginsys.forms import UserForm


class LoginView(generic.View):
    template_name = 'loginsys/login.html'

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('blog:index')

        return render(request, self.template_name)


class UserFormView(generic.View):
    template_name = 'loginsys/register.html'

    def get(self, request):
        form = UserForm(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = auth.authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    auth.login(request, user)
                    return redirect('blog:index')

        return render(request, self.template_name, {'form': form} )



class LogoutView(generic.View):

    def get(self, request):
        auth.logout(request)
        return redirect('blog:index')




