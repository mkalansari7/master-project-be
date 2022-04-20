from dataclasses import fields
from rest_framework import serializers
from .models import Team

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'