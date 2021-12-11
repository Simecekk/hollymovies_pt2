from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import AuthenticationForm

from movie.forms.accounts import RegistrationForm


class RegistrationView(FormMixin, TemplateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account {form.cleaned_data["username"]} created')
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Something wrong')
            return TemplateResponse(request, 'accounts/registration.html', context={'form': form})


class LoginView(FormMixin, TemplateView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Log in successfully')
            return redirect('homepage')

        messages.error(request, 'Wrong Credentials')
        return redirect('auth:login')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Log out successfully')
        return redirect('homepage')
