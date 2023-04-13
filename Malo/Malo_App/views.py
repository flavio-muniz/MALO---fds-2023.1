from django.shortcuts import render,redirect
import calendar
from django.http import HttpResponse
from calendar import HTMLCalendar
from datetime import datetime,date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Ingredient,Table
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return redirect('logina')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calendario')
        else:
        # Return an 'invalid login' error message.Ironicamente messages.sucess
            messages.success(request,("There Was An Error Loggin In, Try Again..."))
            return redirect('logina')
    else:
        return render(request, 'login.html',{})



def All_ingredient(request):
    ingredient_list = Ingredient.objects.all()
    return render(request,'listadeingredientes.html',{
        'ingredient_list':ingredient_list,
    })
