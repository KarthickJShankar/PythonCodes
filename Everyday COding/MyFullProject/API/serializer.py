from MyFullApp import models
from rest_framework import serializers

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyModel
        fields = '__all__'
