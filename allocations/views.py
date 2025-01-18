from rest_framework import viewsets
from .models import Allocation
from .serializers import AllocationSerializer

class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
