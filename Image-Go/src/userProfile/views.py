from django.shortcuts import render, reverse, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout





class User_login(LoginView):
	template_name = "login.html"
	redirect_authenticated_user = True
	authentication_form = AuthenticationForm

	def get_success_url(self):
		return reverse("main:loginHome")


def Add_newUser(request):
	if request.method == "POST":
		if request.POST['pwd1'] == request.POST['pwd2']:

			try:
				user = User.objects.get(username=request.POST['name'])
				return render(request,"register.html", {'error' :"User Already exit"})
			except User.DoesNotExist:
				user = User.objects.create_user(username =request.POST['name'], password = request.POST['pwd1'])
				return redirect (reverse("main:home"))

		else:
			return render(request,"register.html", {'error' :"Password do not match"})

	else:
		return render(request,"register.html")

	

def user_logout_view(request):
	logout(request)
	return redirect(reverse("main:home"))

'''
from userProfile.forms import SignUp_Form
class Add_newUser(CreateView):
	models = User
	form_class = SignUp_Form
	template_name = "register.html"

	def form_valid(self):
		form = super().form_valid(form)
		form.save()
		user = authenticate(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password2'))
		login(self, request, user)
		return redirect(reverse("main:home"))

	def get_success_url(self):
		return reverse("main:login")
		'''