from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mylist/",include("Tasks_feature.urls")),
    
]
