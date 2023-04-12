from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calendario')
        else:
        # Return an 'invalid login' error message.
            messages.success(request,("There Was An Error Loggin In, Try Again..."))
            return redirect('calendario')
    
    else:
        return render(request, 'events/login.html',{})

def calendario(request,year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Victor"
    month = month.capitalize() #convertendo para minúsculo
    #convertendo mes de string para int
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #criando calendário
    cal = HTMLCalendar().formatmonth(year,month_number)

    #pegando o ano atual
    now = datetime.now()
    current_year = now.year

    #pegando o tempo atual
    time= now.strftime('%I:%M:%S %p')
    return render(request, 'events/calendario.html',{
        "first_name" : name,
        "year" : year,
        "month" : month,
        "month_number" : month_number,
        "cal": cal,
        "current_year" : current_year,
        'time' : time,
    })
