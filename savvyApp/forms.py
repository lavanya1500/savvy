from django import forms 
from .models import SignUp, Complaints, LogIn 

class SignUpForm(forms.ModelForm):
    class Meta:
        model= SignUp
        fields=['firstname', 'lastname', 'email', 'password', 'address']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model= Complaints
        fields=['selectcategory','address','city','state','zip','landmark','photo']

class LogInForm(forms.ModelForm):
    class Meta:
        model=LogIn
        fields=['email','password']
        