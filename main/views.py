from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Script
from .serializers import ScriptSerializer

class ScriptListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = []
    pagination_class = LimitOffsetPagination
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

class ScriptRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer