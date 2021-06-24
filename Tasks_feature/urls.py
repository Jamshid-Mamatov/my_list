from django.urls import path
from . import views
urlpatterns=[
    path('',views.addTask),
    path("del/",views.delTask),
    path("update/",views.updatetask),
]