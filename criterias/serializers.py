from dataclasses import fields
from rest_framework import serializers
from .models import Criteria

class CriteriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'