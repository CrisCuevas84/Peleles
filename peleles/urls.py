from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('peleles', views.otro_metodo), 
]
