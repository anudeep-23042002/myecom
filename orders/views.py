from django.shortcuts import render
from contextlib import redirect_stderr
from itertools import product
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from home.models import Cart,Item,Orders
def addorder(request):
    if(request.method=="POST"):
        user_id=request.POST['userid']
        product_id=request.POST['productid']
    return redirect('/')
def order_view(request):
    if(request.method=='POST'):
        user_id=request.POST['user_id']
        order=Orders.objects.filter(user=user_id)
        return render(request,"order.html",{'ord':order})
    return redirect('/')
def checkout(request):
    user_id=request.POST['userid']
    product_id=request.POST['productid']
    item=Item.objects.filter(id=product_id)
    return render(request,"checkout.html",{'name':item[0].name,'discount_price':item[0].discount_price,'sum':0})
