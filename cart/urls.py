from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.addcart),
    path('view/',views.cart_view),
]