from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllocationViewSet

router = DefaultRouter()
router.register(r'allocations', AllocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
