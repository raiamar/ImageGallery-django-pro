from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserAuthForm(AuthenticationForm):
	pass

'''
class SignUp_Form(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ("username", "email", "password1","password2")


		widgets = {
			'username' : forms.Textarea(attrs={'class': 'form-control'}),
		}
	
'''