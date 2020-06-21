from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
	
	title=forms.CharField(widget= forms.TextInput(attrs={'placeholder':" What's New "}))

	class Meta:
		model  = Task
		fields = '__all__'

		
