from django.db import models

# Create your models here.
class Semester(models.Model):
    name = models.CharField(max_length=255)