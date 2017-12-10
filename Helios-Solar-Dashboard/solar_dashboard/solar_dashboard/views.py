from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

def dashboard(request):
   return render(request, 'index.html')