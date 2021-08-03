from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignupApi.as_view()),
    path('placeorder/',Placeorder.as_view()),
    path('additem/',AddItem.as_view()),
    path('addmenu/',AddMenu.as_view()),
    path('addrestaurant/',AddRestaurant.as_view()),
    path('allrestaurant/',ShowAllRestaurant.as_view()),
    path('showitem/',ShowItem.as_view()),
    path('showmenu/',ShowMenu.as_view()),
    path('deleterestaurant',DeleteRestaurant.as_view()),
    path('updaterestaurant',UpdateRestaurant.as_view())

]
