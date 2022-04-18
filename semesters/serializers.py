from dataclasses import fields
from rest_framework import serializers
from .models import Semester

class SemesterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
        