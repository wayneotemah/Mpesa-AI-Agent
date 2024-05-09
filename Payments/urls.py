from django.urls import path

from . import views

urlpatterns = [
    path('mpesa/', views.mpesa, name='mpesa'),
]
