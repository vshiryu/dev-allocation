from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TechnologyViewSet

router = DefaultRouter()
router.register('technologies', TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
