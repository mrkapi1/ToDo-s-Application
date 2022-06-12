from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="deleteTask"),
]