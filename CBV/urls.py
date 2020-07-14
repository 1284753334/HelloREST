from django.conf.urls import url
from CBV import views

app_name = 'cbv'
urlpatterns = [
    url(r'^hello/',views.HelloCBV.as_view(msg = '77777'),name='hello'),
    url(r'^book/',views.BookCBV.as_view(),name='book'),

]

