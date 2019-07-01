from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Task, Team
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

	def get_context_data(self, **kwargs):
		context = super(TaskListView, self).get_context_data(**kwargs)
		context['tasks'] = Task.objects.filter(status='TD').filter(assignee=self.request.user).filter(parent=None).order_by('due')
		context['done'] = Task.objects.filter(status='D').filter(assignee=self.request.user).filter(parent=None).order_by('due')
		context['pend'] = Task.objects.filter(status='P').filter(assignee=self.request.user).filter(parent=None).order_by('due')
		context['width'] = '4'
		return context


class UserTaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'todo_list/user_tasks.html'
	ordering = ['due']
	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Task.objects.filter(assignee=user).filter(parent=None).order_by('due')

	def get_context_data(self, **kwargs):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		context = super(UserTaskListView, self).get_context_data(**kwargs)
		context['user'] = user
		context['tasks'] = Task.objects.filter(status='TD').filter(assignee=user).filter(parent=None).order_by('due')
		context['done'] = Task.objects.filter(status='D').filter(assignee=user).filter(parent=None).order_by('due')
		context['pend'] = Task.objects.filter(status='P').filter(assignee=user).filter(parent=None).order_by('due')
		context['width'] = '4'
		return context


def completeTodo(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	if task.assignee == request.user:
		task.status = 'D'
		task.save()

	return redirect('todo_list-personal')

def acceptTodo(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	if task.assignee == request.user:
		task.status = 'TD'
		task.save()

	return redirect('todo_list-personal')

def doTodo(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	if task.assignee == request.user:
		task.status = 'TD'
		task.save()

	return redirect('todo_list-personal')


class TeamDetailView(LoginRequiredMixin, DetailView):
	model = Team
	context_object_name = 'team'
	template_name = 'todo_list/team_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(TeamDetailView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context


class TaskDetailView(LoginRequiredMixin, DetailView):
	model = Task
	context_object_name = 'tasks'
	template_name = 'todo_list/task_detail.html'
	queryset = Task.objects.all()

	def get_context_data(self, **kwargs):
		context = super(TaskDetailView, self).get_context_data(**kwargs)
		context['main'] = self.get_object()
		context['sub'] = Task.objects.filter(parent=self.get_object())
		context['width'] = '8'
		return context

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Task
	success_url = '/dashboard/'
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.assigner:
			return True
		return False

	def get_context_data(self, **kwargs):
		context = super(TaskDeleteView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Team
	success_url = '/dashboard/team/'
	def test_func(self):
		team = self.get_object()
		if self.request.user == team.leader:
			return True
		return False

		def get_context_data(self, **kwargs):
			context = super(TeamDeleteView, self).get_context_data(**kwargs)
			context['width'] = '8'
			return context

class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	fields = ['name', 'assignee', 'description', 'due']
	
	def form_valid(self, form):
		form.instance.assigner = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(TaskCreateView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context

class TeamCreateView(LoginRequiredMixin, CreateView):
	model = Team
	fields = ['name', 'description', 'members']
	
	def form_valid(self, form):
		form.instance.leader = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(TeamCreateView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context


def subtaskView(request, todo_id):
	task_parent = Task.objects.get(pk=todo_id)
	task_child = Task(name=None, description= None, assigner=request.user, assignee=None, parent=task_parent)
	task_child.save()
	url = '/dashboard/task/'+ str(task_child.id) +'/update/'
	return redirect(url)

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

	def get_context_data(self, **kwargs):
		context = super(TaskUpdateView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context

class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Team
	fields = ['name', 'description', 'members']
	
	def form_valid(self, form):
		form.instance.leader = self.request.user
		return super().form_valid(form)

	def test_func(self):
		team = self.get_object()
		if self.request.user == team.leader:
			return True
		return False

	def get_context_data(self, **kwargs):
		context = super(TeamUpdateView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context

class TeamListView(LoginRequiredMixin, ListView):
	model = Team
	template_name = 'todo_list/team.html'
	context_object_name = 'teams'
	
	def get_queryset(self):
		return Team.objects.filter(leader=self.request.user)

	def get_context_data(self, **kwargs):
		context = super(TeamListView, self).get_context_data(**kwargs)
		context['width'] = '8'
		return context

