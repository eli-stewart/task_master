from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('first_name')
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
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()	
			p_form.save()
			messages.success(request, f'Account updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


	context = {
		'u_form': u_form,
		'p_form': p_form,
		'name': 'Profile'
	}
	return render(request, 'users/profile.html', context)


