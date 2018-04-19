from django.contrib import admin
from django.urls import path,include
from .views import cards

urlpatterns = [
    path('cards', cards),
]
