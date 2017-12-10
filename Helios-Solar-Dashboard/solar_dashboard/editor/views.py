from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from functions import QueryHandler

#Determines action to take depending on request method
def editor (request):
   if request.method == 'GET':
      return editor_form(request)
   elif request.method == 'POST':
       return update_settings(request)

#Sends user to editor if logged in, redirects to login page otherwise
def editor_form(request):
   if 'name' in request.session:
      return render(request, 'adminDash.html')
   else:
      return HttpResponseRedirect('/login')

#Updates the dashboard settings with the values in the submitted form
def update_settings(request):
   QueryHandler.update_dashboard_settings(request.POST)
   return HttpResponseRedirect('/editor')