from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

def check_auth(request):
    if request.user.is_authenticated:
        return 1#HttpResponse("Пользователь авторизован", status=200)
    else:
        return 0#redirect('user:login') 

def index(request:HttpRequest)->HttpResponse:
    return redirect('user:profile')
    """if check_auth(request):
        return redirect('user:profile')
    else:
        return redirect('user:login')"""

#@login_required
def profile(request:HttpRequest)->HttpResponse:
    return HttpResponse('123')

def login(request:HttpRequest)->HttpResponse:
    return render(request,'login.html')

def register(request:HttpRequest)->HttpResponse:
    return render(request,'register.html')