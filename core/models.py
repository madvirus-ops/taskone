from random import choices
from django.db import models

# Create your models here.

class ArithmeticModel(models.Model):
    """to save operations"""
    x = models.IntegerField()
    y = models.IntegerField()

    #Texchoices inherit enums in django
    class Operation(models.TextChoices):
        ADDITION = 'addition'
        MULTIPLICATION = 'multiplication'
        SUBTRACTION = 'subtraction'

    operation_type = models.CharField(max_length=255,choices=Operation.choices,)

    def __str__(self):
        return f'result for {self.x} and {self.y}'



