from django.urls import path
from .views import TeamDeleteView, TeamUpdateView, TeamCreateView, TeamDetailView, TeamListView, TaskDeleteView, TaskUpdateView, TaskListView, UserTaskListView, TaskDetailView, TaskCreateView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='todo_list-personal'),
    path('user/<str:username>', UserTaskListView.as_view(), name='user-tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('team/new/', TeamCreateView.as_view(), name='team-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('team/<int:pk>/update/', TeamUpdateView.as_view(), name='team-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('team/',TeamListView.as_view(), name='todo_list-team'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    #path('complete2/<todo_id>/<username>/', views.completeTodo2, name='complete2'),
    path('task/<todo_id>/subtask/', views.subtaskView, name='task-subtask'),
]

#app/model_viewtype.html