from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path("add_task/", views.add_task, name="add_task"),
]
