from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from home.models import Item,Orders
def placeorder(request):
    if(request.method=="POST"):
        user_id=request.POST['user_id']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        pro=request.POST['pro']
        Orders(user=user_id,address=address,city=city,state=state,zip=zip,pro=pro,sum=0).save()
    return redirect('/')
