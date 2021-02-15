from django.db import models
from django.forms import ModelForm,Textarea
from django import forms
from .models import  *
class SignupForm(ModelForm):

    class Meta:
      model=Seeker
      fields = ["name","email","mno","password"]
class SigninForm(ModelForm):
   class Meta:
      model=Seeker
      fields = ["email","password"]

