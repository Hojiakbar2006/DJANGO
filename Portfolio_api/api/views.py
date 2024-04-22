from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from api.models import Projects

from .serializers import ProjectsSerializer


class ProjectsListView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


ProjectsListView = ProjectsListView.as_view({'get': 'list', 'post': 'create'})


class ProjectsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'form_errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
