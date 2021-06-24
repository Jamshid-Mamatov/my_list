from django.shortcuts import render
from django.http import JsonResponse
from tinydb import TinyDB,Query

db=TinyDB('database.json')

Tasks=Query()

data={}

# db.truncate()

def addTask(request):
    # print(request.method)  
    
    # print(number)
    
    if request.method=="GET":

        task_name=request.GET.get('task')
        if task_name!=None:
            db.insert({'task':task_name})
            # number=len(db.all())
            # print(number)
            lst=db.all()
            # data['tasks']=lst
            # item=db.search(Tasks.task==task_name)
        
        
            # data[number]=item[-1]
            for ind,val in enumerate(lst):
                data[str(ind+1)+"-task"]=val

    print(data)

    # print(task_name)
    return JsonResponse(data)



