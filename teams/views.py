from rest_framework.viewsets import ModelViewSet
from .models import Team
from .serializers import TeamListSerializer

# Create your views here.

class TeamListSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
