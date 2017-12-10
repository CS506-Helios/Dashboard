from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from functions import QueryHandler
from functions import DataCalculator
import datetime

def data(request):
    timescale = request.GET['timescale']
    
    #num_days is the number of days prior to today for which data needs to be collected
    num_days = None 

    #Determine the value of num_days
    if timescale == 'week':
        num_days = datetime.datetime.today().weekday()
    elif timescale == 'month':
        num_days = datetime.datetime.today().day
    elif timescale == 'year':
        num_days = datetime.datetime.today().month
    else:
        return HttpResponseBadRequest("Not a valid request")

    #Get energy data for num_days
    energy_data = QueryHandler.energy_data(num_days, timescale)

    #Prepare response dict
    result = {}

    #Get array containing the individual energy total for the days or months
    individual_energy_totals = DataCalculator.individual_energy_totals(energy_data, timescale)
    result['values'] = individual_energy_totals

    #Get total energy for the timescale
    total_energy = DataCalculator.total_energy(individual_energy_totals)

    #Calculate energy analogy value
    energy_unit = QueryHandler.energy_analogy()
    analogy_value = DataCalculator.energy_analogy_value(total_energy, energy_unit)
    result['energyAnalogyValue'] = analogy_value

    #Calculate money saved
    price_per_kwh = QueryHandler.energy_price()
    money_saved = DataCalculator.money_saved(total_energy, price_per_kwh)
    result['moneySaved'] = money_saved

    #Calculate percentage
    energy_percentage = DataCalculator.energy_percentage(total_energy, 6)
    result['percentage'] = energy_percentage

    #Return JSON data
    return JsonResponse(result)