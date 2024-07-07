
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignUpForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            # need an error message
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home:home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home:home')
        
    else:
        form = SignUpForm

    return render(request, 'register.html', {"form": form})


def login_register(request):
    return render(request, 'login_or_register.html', {})

