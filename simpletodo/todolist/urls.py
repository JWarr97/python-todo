from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('<int:pk>/', views.todo, name='todo')
]