from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def dashboard(request):

    return render(request,'account/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {
    'form':form,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:dashboard')
            else:
                messages:info(request, 'Username OR password is incorrect')

    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)
    return redirect('account:login')

def profile_settings(request):

    return render(request,'account/profile.html',)
