from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HotelViewset

router = DefaultRouter()
router.register('', HotelViewset,)

urlpatterns = [
    path('', include(router.urls)),
]