from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from App import views

app_name = 'app'
urlpatterns = [
   url(r'^index/',views.index,name='inndex') ,
]
