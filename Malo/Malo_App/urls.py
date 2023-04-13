from django.urls import path
from . import views

urlpatterns = [
    # Path Convertes
    # int: numbers
    # str: strings
    # path: todas urls
    # slug: hyphen-and_underscores_stuff
    # UUID: universally unique identifier
    # path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.calendario, name="calendario"),
    path('home/', views.calendario, name="calendario"),
    path('login/', views.login_user, name="login"),
]