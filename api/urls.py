from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
    url(r'^book/$', views.book, name='book'),
    url(r'^books/(?P<bookid>\d+)/', views.books, name='books'),
]
