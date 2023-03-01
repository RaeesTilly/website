# created the bandapp urls
from django.urls import path
from . import views

app_name = 'bandapp'
urlpatterns = [
    path('', views.bandapp, name='bandapp'),
]