from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('signup/',views.SignupPage,name='signup'),
    path('', views.login_user, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage,name='logout'),
    path('listadeingredientes/', views.All_ingredient, name='ingredient_list'),
    path('add-ingredientes/', views.Add_ingredient, name='add_ingredient'),
    path('menu/', views.Menu, name='menu'),
    path('add-dishes/', views.Add_dish, name='add_dish'),
    path('edit-dish/<dish_id>', views.Edit_dish, name='edit_dish'),
    path('mesa/', views.all_Mesa, name='mesa'),
    path('add_mesa', views.add_mesa, name='add_mesa'),
]

