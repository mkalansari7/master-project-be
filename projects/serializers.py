from dataclasses import fields
from rest_framework import serializers
from .models import Project
from teams.views import TeamListSerializer
from evaluations.serializers import EvaluationListSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    team = TeamListSerializer(many=True, read_only=True)
    linkId = EvaluationListSerializer(read_only= True)
    class Meta:
        model = Project
        fields = '__all__'