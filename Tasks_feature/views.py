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
            lst=db.all()
            db.insert({'task'+str(len(lst)+1):task_name})
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

def delTask(request):
    task_name=request.GET.get('task')
    data={}
    if task_name!=None:
        db.remove(Tasks.task==task_name)
        lst=db.all()
        print(lst)
        
        for ind,val in enumerate(lst):
            
            data[str(ind+1)+"-task"]=val
        
        
            
    return JsonResponse(data)


def updatetask(request):
    data={}
    
    task_name=request.GET.get()
    print(task_name)
    db.update({"task":task_name},Tasks.task.exists())
    lst=db.all()
    print(lst)
    for ind,val in enumerate(lst):
            
        data[str(ind+1)+"-task"]=val

    return JsonResponse(data)