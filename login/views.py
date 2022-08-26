from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from home.models import Category, Item
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        pass1 = request.POST['pass']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('/')
    return render(request,'login.html')