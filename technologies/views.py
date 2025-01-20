from rest_framework import viewsets
from .models import Technology
from .serializers import TechnologySerializer
from rest_framework.permissions import IsAuthenticated

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated]
