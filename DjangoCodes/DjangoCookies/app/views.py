from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def index(req):
#     response = HttpResponse("<h1>Setting Cookie Example</h1>")
#     response.set_cookie("bmpl","This is cookie example")
#     # render(req, 'index.html')
#     return response
#
# def showCookies(req):
#     show = req.COOKIES['bmpl']
#     return HttpResponse("<h2>New Data {}</h1>".format(show))

def setCookie(req):
    html = HttpResponse("<h1>Basic Cookie Example</h1>")
    if req.COOKIES.get('visited'):
        html.set_cookie('bmpl','Welcome Back')
        value = int(req.COOKIES.get('visited'))
        html.set_cookie('visited',value + 1)
    else:
        value = 1
        text = "Welcome, You appeared for the first time"
        html.set_cookie('visited',value)
        html.set_cookie('bmpl',text)
    return html

def getCookie(req):
    if req.COOKIES.get('visited'):
        value = req.COOKIES.get('visited')
        text = req.COOKIES.get('bmpl')
        html = HttpResponse("<h2>{}, You have visited this page {} time</h1>".format(text,value))
        html.set_cookie('visited',str(int(value) + 1))
        return html
    else:
        return redirect('/setCookie')