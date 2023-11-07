from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, FormView
from django.contrib.auth import authenticate
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
        succes_message = messages.success(request, 'succeed')
        return redirect('login')


class Signup(FormView):
    form_class = CreateUserForm
    template_name = 'signup.html'
    success_url = '/accounts/login/'

    # def form_valid(self, form):
    #     form.save()
    #     success_message = messages.success(self.request, 'Success!')
    #     return super().form_valid(form)
    

    # def form_valid(self, form):
    #     user = form.save()
    #     messages.success(self.request, 'Account created successfully. You can now log in.')
    #     return self.render_to_response(self.get_context_data(form=form, success=True))


    def form_valid(self, form):
            user = form.save()
            messages.success(self.request, 'Account created successfully. You can now log in.')
            return super().form_valid(form)