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
    path('', views.home, name='home'),
    path('login/', views.login_user, name='logina'),
    path('listadeingredientes/', views.All_ingredient, name='ingredient_list'),
]
