from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def addTask(request):
    
    return JsonResponse({"a":1,'c':[{'b':2},{'c':3}]})

