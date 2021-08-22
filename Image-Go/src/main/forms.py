
from main.models import Image_model
from django import forms
from django.db.models import fields

class Image_upload_form(forms.ModelForm):
	class Meta:
		model = Image_model
		# fields = '__all__'
		fields = ('imageTitle', 'image_Type', 'description', 'image_Category', 'imageUpload', 'imageData')


		widgets = {
			'imageTitle' : forms.TextInput(attrs={'class' : 'form-control'}),
			'description' : forms.Textarea(attrs={'class' : 'form-control'}),
			'imageUpload':forms.FileInput(attrs={'class' : 'form-control'}),
			'image_Category':forms.Select(attrs={'class' : 'form-control'}),
			'image_Type':forms.Select(attrs={'class' : 'form-control'}),
			# 'owner':forms.Select(attrs={'class' : 'form-control'}),
		}

	


