from rest_framework import serializers
from .models import Judge


class JudgeCreateSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()
    class Meta:
        model= Judge
        fields = "__all__"

    def create(self, validated_data):
        defCriteria = []
        for criteria in validated_data['evaluation'].project.criteria.all():
            defCriteria.append({"criteria_id": criteria.id, "criteria_name":criteria.name, "criteria_weight":criteria.weight, "grade":0})
        teams = []
        for team in validated_data['evaluation'].project.team.all():
            teams.append({"team_id":team.id, "team_name":team.name,"grade":defCriteria, "note":""})
        validated_data['grade'] = teams
        return super().create(validated_data)  
        


class JudgeListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Judge
        fields = "__all__"