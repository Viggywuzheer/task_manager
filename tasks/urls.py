# tasks/urs.py
from django.urls import path
from .views import TaskListView

urlpatterns = [
        path('', TaskListView.as_view(), name = 'task-list'),
]

