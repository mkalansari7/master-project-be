from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectListSerializer

# Create your views here.

class ProjectListSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer