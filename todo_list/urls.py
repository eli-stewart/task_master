from django.urls import path
from . import views

urlpatterns = [
    path('',views.personal, name='todo_list-personal'),
    path('team/',views.team, name='todo_list-team'),
]