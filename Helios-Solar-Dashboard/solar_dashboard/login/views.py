from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from functions import QueryHandler

def login(request):
    if request.method == 'GET':
        return login_form(request)
    elif request.method == 'POST':
        return authenticate(request)

#Handles request for the login form
def login_form(request):
    return render(request, 'login.html')

#Handles admin authentication and login
def authenticate(request):
    username = request.POST['uname']
    password = request.POST['psw']

    username_password = QueryHandler.authenticate(username)
    if username_password != None and username_password[1] == password:
        return HttpResponse("<h1>You in</h1>")
    else:
        return HttpResponseRedirect('/login')