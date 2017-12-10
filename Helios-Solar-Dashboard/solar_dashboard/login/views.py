from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from functions import QueryHandler

#Determines action to take depending on request method
def login(request):
    if request.method == 'GET':
        return login_form(request)
    elif request.method == 'POST':
        return authenticate(request)

#Handles request for the login form
def login_form(request):
    if 'name' in request.session:
        #Redirect to dashboard editor if the admin is already logged in
        return HttpResponse("<h1>The key exists</h1>")
    else:
        #Return login form if admin is not logged in
        return render(request, 'login.html')

#Handles admin authentication and login
def authenticate(request):
    username = request.POST['uname']
    password = request.POST['psw']

    username_password = QueryHandler.authenticate(username)
    if username_password != None and username_password[1] == password:
        #Login Succeeded

        #Create session
        request.session['name'] = username

        #Redirect to dashboard editor
        return HttpResponseRedirect('/editor')
    else:
        #Logn Failed

        #Reload login form
        return HttpResponseRedirect('/login')