from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	name = forms.CharField(max_length=100, required = True)
	email = forms.EmailField()
	phone = forms.CharField(max_length=100, required = False)
	office = forms.CharField(max_length=100, required = False)

	class Meta:
		model = User
		fields = ['name', 'username', 'email', 'phone', 'office', 'password1', 'password2' ]
