from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(req):
#     return HttpResponse("<h1>This is django hello world</h1>")

def index(req):
    x = 10
    y = 12
    z = x + y
    return render(req,'index.html',context={'result':z})

def login(req):
    return render(req, 'login.html')