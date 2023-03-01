# created the bandapp urls
from django.urls import path
from . import views
"""created
bandapp and url patterns
"""
app_name = 'bandapp'
urlpatterns = [
    path('', views.bandapp, name='bandapp'),
]