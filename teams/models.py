from django.db import models
from projects.models import Project

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team')
