from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Akun_form(UserCreationForm):
	class Meta:
		model = Akun
		fields = '__all__'