from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        user = User.objects.create_user(username=username, password = password1)     
        user.save()   
        messages.success(request, 'Your account has been created')
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'account verified!')
            return render(request, 'dashboard.html', {"username":username})
    return render(request, 'signin.html')