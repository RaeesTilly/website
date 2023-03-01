from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_l:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_l:show_user'))

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user1.html', {
        'username': request.user.username,
        'password': request.user.password
    })            