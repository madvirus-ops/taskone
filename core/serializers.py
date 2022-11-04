
from rest_framework import serializers
from .models import ArithmeticModel


class ArithmeticSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArithmeticModel
        fields = ('x','y','operation_type',)