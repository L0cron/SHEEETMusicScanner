
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def index(request:HttpRequest)->HttpResponse:
    return render(request,'index.html')

