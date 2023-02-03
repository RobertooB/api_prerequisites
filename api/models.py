from django.db import models

# Create your models here.

class Prerequisites (models.Model):
    name = models.CharField(max_length=30)
    observation = models.CharField(max_length=150)
    route = models.CharField(max_length=500)
    state = models.BooleanField()
    
class PrerequisitesForm (models.Model):
    prerequisites = models.ForeignKey(Prerequisites, on_delete=models.PROTECT)
    form = models.IntegerField()
