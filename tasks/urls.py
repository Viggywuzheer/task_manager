from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView

urlpatterns = [
        path('',TaskListView.as_view(), name='task-list'),
        path('add/', TaskCreateView.as_view(), name = 'task-add'),
        path('<int:pk>/edit/', TaskUpdateView.as_view(), name = 'task-edit'),
]
