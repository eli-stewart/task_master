from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('name')
			messages.success(request, f'Welcome {name}! Log In Below')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = {
		'form': form,
		'name': 'Sign Up for Task Manager',
	}
	return render(request, 'users/register.html', context)

@login_required
def profile(request):
	context = {
		'name': 'Profile',
	}
	return render(request, 'users/profile.html', context)


