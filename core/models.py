from random import choices
from django.db import models

# Create your models here.

class ArithmeticModel(models.Model):
    """to save operations"""
    x = models.IntegerField()
    y = models.IntegerField()
    operation_type = models.CharField(max_length=255)

    def add(self):
        pass


    def __str__(self):
        return f'result for {self.x} and {self.y}'



