from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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


class ScriptRetrieveByNameView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if name:
            queryset = Script.objects.filter(name__icontains=name)
        else:
            queryset = Script.objects.all()
        serializer = ScriptSerializer(queryset, many=True)
        return Response(serializer)

class ScriptRetrieveByNoOfRecords(APIView):

    def get(self, request):
        offset = int(request.query_params.get('offset'))
        limit = int(request.query_params.get('limit'))
        if offset and limit:
            queryset = Script.objects.all()[offset: offset+limit]
        else:
            queryset = Script.objects.all()
        serializer = ScriptSerializer(queryset, many=True)
        return Response(serializer)
