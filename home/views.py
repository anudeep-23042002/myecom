from django.shortcuts import render

from .models import Category, Item,Cart

# Create your views here.
def home(request):
    dest=Item.objects.all()
    categories=Category.objects.all();
    return render(request,'hom.html',{'dests':dest , 'categories':categories})
