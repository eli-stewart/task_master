from django.shortcuts import render
from django.http import HttpResponse
from .models import Task




# Create your views here.
def personal(request):
	context = {
		'tasks': Task.objects.all(),
		'name': 'Personal Dashboard',
	}
	return render(request, 'todo_list/personal.html', context)

def team(request):
	context = {
		'name': 'Team Dashboard',
	}
	return render(request, 'todo_list/team.html', {'name': 'Team Dashboard'})