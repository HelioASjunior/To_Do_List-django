from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('toggle/<int:id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]