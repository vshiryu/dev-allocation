from rest_framework import viewsets
from .models import Allocation
from .serializers import AllocationSerializer
from rest_framework.permissions import IsAuthenticated

class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    permission_classes = [IsAuthenticated]
