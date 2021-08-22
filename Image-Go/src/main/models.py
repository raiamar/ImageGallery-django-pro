from django.db import models
from django.contrib.auth.models import User

class Image_cat(models.Model):
	category = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.category

class Image_model(models.Model):
	IMAGE_TYPE = [
		('Free', 'Free'),
		('Paid', 'Paid'),
		]
	imageTitle = models.CharField(max_length = 25, verbose_name = "Image Title")
	image_Type = models.CharField(max_length=5, choices =IMAGE_TYPE, default= 'Free', null=True, blank=True, verbose_name = "Image Type")
	description = models.TextField()
	image_Category = models.ForeignKey(Image_cat, on_delete=models.CASCADE, null=True, blank=True, verbose_name = "Categoty")
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	imageUpload = models.ImageField(upload_to = "Image_upload/", verbose_name = "Image") 
	imageData =models.BooleanField(default=True, verbose_name = "Is Your image raw", null=True, blank=True)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.imageTitle

	