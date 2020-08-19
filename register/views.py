from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages as m

# Create your views here.
def register(response):
    if response.method=='POST':
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(response,'main/errorregister.html',{})
    else:
        form=RegisterForm()
    return render(response,'register/register.html',{'form':form})
