# urls for the login/authentication page
from django.urls import path, include
from . import views

app_name = 'user_l'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
]