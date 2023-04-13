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
    path('',views.home, name="home"),
    path('<int:year>/<str:month>/', views.calendario, name="calendariodigitado"),
    path('calendar/', views.calendario, name="calendario"),
    path('login/', views.login_user, name="logina"),
    path('ingredientes/', views.All_ingredient,name="ingredient_list"),
    path('adicionar_mesa/', views.adicionar_mesa, name='adicionar_mesa'),
     path('mesa/', views.adicionar_mesa, name='mesa_list'),
]