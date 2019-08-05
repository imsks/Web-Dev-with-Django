from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.aboutUs, name="aboutUs"),
    path('contact/', views.contactUs, name="contactUs"),
    path('tracker/', views.trackingStatus, name="trackingStatus"),
    path('search/', views.search, name="search"),
    path('products/<int:myid>', views.products, name="products"),
    path('checkout/', views.checkout, name="checkout"),
]