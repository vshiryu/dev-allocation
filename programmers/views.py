from rest_framework import viewsets
from .models import Programmer
from .serializers import ProgrammerSerializer
from rest_framework.permissions import IsAuthenticated

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = [IsAuthenticated]
