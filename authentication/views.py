from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print(request.POST)
        user = User()
        # id = request.for
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return redirect('login')
    return render(request, 'authentication/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        
        try:
            user = User.objects.get(email=email)
        except:
            print('User not found')
            messages.error(request, 'User not found')
            
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Invalid credentials')
            messages.error(request, 'Invalid credentials')
            
    return render(request, 'authentication/login.html')

def home(request):
    return render(request, 'authentication/home.html')