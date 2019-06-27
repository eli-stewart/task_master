from django.urls import path
from .views import TaskDeleteView, TaskUpdateView, TaskListView, UserTaskListView, TaskDetailView, TaskCreateView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='todo_list-personal'),
    path('user/<str:username>', UserTaskListView.as_view(), name='user-tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('team/',views.team, name='todo_list-team'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
]

#app/model_viewtype.html