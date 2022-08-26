from django.urls import path
from . import views
urlpatterns = [
    path('',views.product,name='product'),
    path('product',views.product),
]