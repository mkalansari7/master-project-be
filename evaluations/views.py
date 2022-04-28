from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Evaluation
from .serializers import EvaluationListSerializer

# Create your views here.
class EvaluationListSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationListSerializer