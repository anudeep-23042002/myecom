from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.order_view),
    path('checkout/',views.checkout),
    path('checkout/order',views.checkout),
]