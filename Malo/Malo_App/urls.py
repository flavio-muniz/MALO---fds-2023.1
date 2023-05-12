from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupPage,name='signup'),
    path('', views.login_user, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage,name='logout'),
    path('ingredient-list/', views.All_ingredient, name='ingredient_list'),
    path('add-ingredientes/', views.Add_ingredient, name='add_ingredient'),
    path('menu-category/', views.Category_menu, name='menu_category'),
    path('add-category/', views.Add_category, name='add_category'),
    path('edit-category/<category_id>', views.Edit_category, name='edit_category'),
    path('delete-category/<category_id>', views.Delete_category, name='delete_category'),
    path('delete-ingredient/<ingredient_id>', views.Delete_ingredient, name='delete_ingredient'),
    path('edit-ingredient/<ingredient_id>', views.Edit_ingredient, name='edit_ingredient'),
    path('menu/', views.Menu, name='menu'),
    path('add-dishes/', views.Add_dish, name='add_dish'),
    path('edit-dish/<dish_id>', views.Edit_dish, name='edit_dish'),
    path('delete-dish/<dish_id>/<origin>', views.Delete_dish, name='delete_dish'),
    path('mesa/', views.all_Mesa, name='mesa'),
    path('add_mesa', views.add_mesa, name='add_mesa'),
    path('add_mult_mesa/', views.add_mult_mesa, name='add_mult_mesa'),
    path('delete_mesa', views.delete_mesa, name='delete_mesa'),
    path('delete_mult_mesa/', views.delete_mult_mesa, name='delete_mult_mesa')
]

