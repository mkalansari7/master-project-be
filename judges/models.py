from django.db import models
from evaluations.models import Evaluation

# Create your models here.
class Judge(models.Model):
    name = models.CharField(max_length=255)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='judge')
    grade = models.JSONField(null = True, blank = True)