from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from functions import query_handler

def data(request):
    result = query_handler.initialize()
    return JsonResponse(result)