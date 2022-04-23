from rest_framework.viewsets import ModelViewSet
from .models import Criteria
from .serializers import CriteriaListSerializer

# Create your views here.

class CriteriaListSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaListSerializer