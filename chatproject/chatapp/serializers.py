from rest_framework import serializers
from .models import ModelProvider

class ModelProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelProvider
        fields = "__all__"
