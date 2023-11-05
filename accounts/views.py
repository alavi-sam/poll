from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib import messages

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