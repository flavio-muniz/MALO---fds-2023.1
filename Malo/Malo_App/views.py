from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Ingredient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, ("Usuário ou senha incorreto!"))
            return redirect('login') 

    return render (request, 'login.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            messages.success(request, ("Suas senhas sao divergentes"))
            return redirect('signup') 
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login') 
        
    return render (request, 'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def All_ingredient(request):
    ingredient_list = Ingredient.objects.all()
    return render(request,'listadeingredientes.html',{
        'ingredient_list':ingredient_list,
    })
