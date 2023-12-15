from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        u = authenticate(request,username=email,password=password)
        if u is not None:
            login(request,u)
            d = u.email
            return HttpResponse("login Succesfull"+d)
        else:
            return HttpResponse("valid")
    return render(request,'loginapp/mylogin.html')
