from django.contrib import admin
from .models import Image_model, Image_cat

@admin.register(Image_model)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('id','imageTitle', 'description', 'imageUpload', 'imageData')
	search_fields = ("id", "imageTitle")


@admin.register(Image_cat)
class Image_cat(admin.ModelAdmin):
	list_display = ("id", "category")

