from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, ComplaintForm, LogInForm
from .models import Complaints
from django.contrib.auth import authenticate,login
from django.contrib import messages
import logging

logger= logging.getLogger(__name__)

def startPage(request):
    return render(request, 'welcome.html')

def loginPage(request):
    if request.method=='POST':
        form= LogInForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('success')
            else:
                form.add_error(None,"Invalid email or password")
    else:
        form=LogInForm()
    return render(request, 'login.html',{'form':form})

def signupPage(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('success')
    else:
        form= SignUpForm()
    return render(request, 'signup.html', {'form':form})

def success_view(request):
    return render(request,'success.html')

def complaintPage(request):
    if request.method == 'POST':
        form= ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complaintPosted')
    else:
        form= ComplaintForm()
    return render(request, 'complaint.html', {'form':form})

def complaintPostedPage(request):
    return render(request,'complaintPosted.html')