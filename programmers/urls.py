from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgrammerViewSet

router = DefaultRouter()
router.register('programmers', ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
