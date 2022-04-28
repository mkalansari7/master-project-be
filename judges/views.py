from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Judge
from .serializers import JudgeCreateSerializer, JudgeListSerializer

# Create your views here.
class JudgeListSet(ModelViewSet):
    queryset = Judge.objects.all()

    # get_Serializers_Class to change the Serializers_Class
    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return JudgeCreateSerializer
        return JudgeListSerializer    
