from django.db import models
from django.forms import ModelForm,Textarea
from django import forms
from .models import  *
class SignupForm(ModelForm):
    class Meta:
      model=Recruiter
      fields = ["name","email","mno","password"]
class SigninForm(ModelForm):
   class Meta:
      model=Recruiter
      fields = ["email","password"]
class JobOpeningForm(ModelForm):
    r=models.IntegerField(max_length="10",editable=False )
    class Meta:
        model=JobOpenings
        fields=["r","job_type","location","keyskills","exprience","designation","area_of_sector","description","salary_range","e_date","p_date"]
