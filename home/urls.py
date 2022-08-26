from django.urls import path
from . import views
from orders import views as v
urlpatterns = [
    path('', views.home),
]