from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AccountViewset,UserRegistrationApiview,activate,UserLoginApiView,UserLogoutView

router = DefaultRouter()
router.register('list', AccountViewset,)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserRegistrationApiview.as_view(),name='register'),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>',activate,name='activate'),
]