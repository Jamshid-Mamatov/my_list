from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from tinydb import TinyDB
db=TinyDB('database.json')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addtask/",include("AddTask_feature.urls"))
]
