from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('signup/', views.signup, name='signup'),
    path('task/<int:id>/toggle/', views.toggle_task, name='toggle_task'),
    path('task/<int:id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:id>/edit/', views.edit_task, name='edit_task'),
]
