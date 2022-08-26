from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from home.models import Item
def product(request,myid):
    pro=Item.objects.filter(id=myid)
    print(pro[0].name)
    return render(request,'product.html',{'pro':pro[0]})