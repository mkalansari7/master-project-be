from re import T
from django.db import models
from semesters.models import Semester
from criterias.models import Criteria

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    wieght = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='project')
    criteria = models.ManyToManyField(Criteria)