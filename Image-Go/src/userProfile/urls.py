from django.urls import path
from userProfile.views import User_login, Add_newUser, user_logout_view

app_name = 'user'

urlpatterns = [
	path('login/', User_login.as_view(), name = "user_login_view"),
	path('register/', Add_newUser, name = "register_new_user" ),
	path("logout/",user_logout_view, name = "logout" )
]


