from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, template_name='login.html')

    def post(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            error_message = messages.error(request, 'invalid credentials')
            return redirect('login')
        login(request, user)
        succes_message = messages.success(request, 'succeed')
        return redirect('login')


class Signup(FormView):
    form_class = CreateUserForm
    template_name = 'signup.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
            user = form.save()
            messages.success(self.request, 'Account created successfully. You can now log in.')
            return super().form_valid(form)