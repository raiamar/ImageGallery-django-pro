from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Image_model
from .forms import Image_upload_form
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def main_page(request):
	Image = Image_model.objects.order_by("-id")
	context = {"Image": Image}
	return render(request, "index.html", context)

def rawImage(request):
	data = Image_model.objects.filter(imageData = True)
	context = {"data" : data}
	return render(request, "rawImage.html", context)

class Add_image(LoginRequiredMixin, CreateView):
	model = Image_model
	form_class = Image_upload_form
	template_name = "form.html"

	def form_valid(self, form):
		# print(form.instance)
		form.save(commit= False)
		form.instance.owner = self.request.user
		form .save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("main:loginHome")

class Edit_image(LoginRequiredMixin, UpdateView):
	model = Image_model
	form_class = Image_upload_form
	template_name = "form.html"

	def get_success_url(self):
		return reverse("main:loginHome")

@login_required(login_url='main:home')
def Delete_image(request, image_model_id):
	Image = Image_model.objects.get(pk = image_model_id)
	Image.delete()
	return HttpResponseRedirect(reverse('main:loginHome'))


'''	
class Delete_image(LoginRequiredMixin, DeleteView):
	model = Image_model
	pk_url_kwarg = 'pk'
	template_name = "form.html"
	def get_success_url(self):
		return reverse("main:loginHome")
'''

def login_home(request):
	#context = {}
	imageData = Image_model.objects.filter(owner__id =request.user.id).order_by("-id")
	context ={"imageData": imageData}
	#context["imageData"] = imageData
	return render(request, "login_user_home.html", context)

def other_Image(request, username):
	owner = get_object_or_404(User, username=username)
	Image = Image_model.objects.filter(owner = get_object_or_404(User, username=username))
	return render(request, "index.html", {'Image': Image})

def search_image(request):
	if request.method == "POST":
		search = request.POST['search']
		Image = Image_model.objects.filter(imageTitle__contains= search )
		return render(request, 'search.html',{'search':search, 'Image':Image})
	else:
		return render(request, 'index.html',{})




