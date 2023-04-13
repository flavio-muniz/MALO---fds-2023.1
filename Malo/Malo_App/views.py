from django.shortcuts import render,redirect
import calendar
from django.http import HttpResponse
from calendar import HTMLCalendar
from datetime import datetime,date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Ingredient

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
            return redirect('calendario')
    else:
        return render(request, 'login.html',{})

def calendario(request, year=None, month=None):
    name = "Gerente"
    now = datetime.now()
    year = year or now.year
    month = month or now.strftime('%B').capitalize()
    month_number = list(calendar.month_name).index(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month_number)
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    day = date.today().strftime("%d")
    return render(request, 'calendario.html',{
        "first_name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
        "day": day,
    })

def All_ingredient(request):
    ingredient_list = Ingredient.objects.all()
    return render(request,'listadeingredientes.html',{
        'ingredient_list':ingredient_list,
    })