from contextlib import redirect_stderr
from itertools import product
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from home.models import Cart,Item
# Create your views here.
def addcart(request):
    if(request.method=="POST"):
        user_id=request.POST['userid'];
        product_id=request.POST['productid']
        product=Item.objects.filter(id=product_id)
        Cart(user=user_id,product=product[0]).save()
    return redirect('/')
def cart_view(request):
    if(request.method=='POST'):
        user_id=request.POST['user_id']
        cart=Cart.objects.filter(user=user_id)
        sum=0;
        for prod in cart:
            sum=sum+(prod.product.discount_price)*(prod.quantity)
        return render(request,'cart.html',{'cart':cart,'sum':sum})
    return redirect('/')
def cart_1(request):
    if(request.method=='POST'):
        qty = request.GET['dropdown'] 
        cart=Cart.objects.filter(user=user_id)
        return render(request,'cart.html',{'cart':cart})
    return redirect('/')
