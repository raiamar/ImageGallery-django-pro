from django.urls import path
from main.views import Add_image, main_page, login_home, Edit_image, Delete_image, rawImage, search_image, other_Image

app_name = 'main'

urlpatterns = [
	path('home/', main_page, name = "home"),
	path('rawImage/', rawImage, name = "rawImage" ),
	path('loginHome/', login_home, name = "loginHome"),
	path('otherImage/<str:username>/', other_Image, name="otherImage"),
	#path('otherImage/<int:user_id>', other_Image, name="otherImage"),
	path('search_image/', search_image, name="search_image"),
	path('add_image/', Add_image.as_view() , name = "new_image_added"),
	path('edit_image/<int:pk>', Edit_image.as_view(), name="edit_image"),
	path('delete_image/<int:image_model_id>', Delete_image, name="delete_image"),	
]


