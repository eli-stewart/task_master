from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Task
from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView




# Create your views here.
def personal(request):
	context = {
		'tasks': Task.objects.all(),
		'name': 'Personal Dashboard',
	}
	return render(request, 'todo_list/personal.html', context)

class TaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'todo_list/personal.html'
	context_object_name = 'tasks'
	ordering = ['due']
	
	def get_queryset(self):
		return Task.objects.filter(assignee=self.request.user).filter(status = 'TD')

class UserTaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'todo_list/user_tasks.html'
	context_object_name = 'tasks'
	ordering = ['due']
	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Task.objects.filter(assignee=user).order_by('due')

def completeTodo(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	if task.assignee == self.request.user:
		task.status = 'D'
		task.save()

	return redirect('todo_list-personal')

class TaskDetailView(LoginRequiredMixin, DetailView):
	model = Task

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Task
	success_url = '/dashboard/'
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.assigner:
			return True
		return False

class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	fields = ['name', 'assignee', 'description', 'due']
	
	def form_valid(self, form):
		form.instance.assigner = self.request.user
		return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Task
	fields = ['name', 'assignee', 'description', 'due']
	
	def form_valid(self, form):
		form.instance.assigner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		task = self.get_object()
		if self.request.user == task.assigner:
			return True
		return False


def team(request):
	context = {
		'name': 'Team Dashboard',
	}
	return render(request, 'todo_list/team.html', {'name': 'Team Dashboard'})