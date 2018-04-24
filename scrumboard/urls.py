"""
in case you need the django to develop for you the default
POST/PUT/DELETE forms and URls

from rest_framework.routers import DefaultRouter
from .api import ListViewSet, CardViewSet

router = DefaultRouter
router.register("lists", ListViewSet)
router.register("cards", CardViewSet)

urlpatterns = router.urls
"""

from django.contrib import admin
from django.urls import path,include
from .views import cards

urlpatterns = [
    path('cards', cards),
]
