from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from home.models import Category, Item
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        user=User.objects.create_user(username=username,password=pass1,email=email)
        user.save()
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request);
    return redirect('/')
