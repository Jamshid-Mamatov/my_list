from django.shortcuts import render
from django.http import JsonResponse
from tinydb import TinyDB,Query
import json

db=TinyDB('database.json')

Tasks=Query()

data={}

# db.truncate()

def addTask(request):
    # print(request.method)  
    
    # print(number)
    
    if request.method=="GET":

        task_name=request.GET.get('task')
        
        db.insert({'task':task_name})
        number=len(db.all())
        print(number)
        item=db.search(Tasks.task==task_name)
        
        
        data[number]=item[-1]

    # print(data)

    # print(task_name)
    return JsonResponse(data)

