from rest_framework.viewsets import ModelViewSet
from .models import Semester
from .serializers import SemesterListSerializer

# Create your views here.

class SemesterListSet(ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterListSerializer