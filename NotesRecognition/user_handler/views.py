from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request:HttpRequest)->HttpResponse:
    return redirect('user:profile')

def profile(request:HttpRequest)->HttpResponse:
    return HttpResponse('123')


def login(request:HttpRequest)->HttpResponse:
    return HttpResponse('123')