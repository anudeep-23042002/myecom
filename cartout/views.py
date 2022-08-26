from django.shortcuts import render,redirect
from home.models import Cart
def cart_checkout(request):
    if request.method=='POST':
        user_id=request.POST['userid']
        cart=Cart.objects.all()
        s=""
        price=0
        org_price=0
        for item in cart:
            if s=="":
                s=s+item.product.name
            else:
                s=s+','+item.product.name
            price=price+item.product.discount_price
            org_price=org_price+item.product.price
        return render(request,"checkout.html",{'name':s,'discount_price':price,'sum':org_price})
    return redirect('/')
