
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def await_approval(request):
    return render(request, 'await_approval.html', {})

@user_passes_test(lambda u: u.is_superuser)
def approve_users(request):
    unapproved_users = User.objects.filter(profile__is_approved=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.profile.is_approved = True
        user.profile.save()
        return redirect('user_auth:approve_users')
    return render(request, 'approve_users.html', {'unapproved_users': unapproved_users})


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

