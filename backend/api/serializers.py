from rest_framework import serializers

from .models import DefaultModel


class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultModel
        fields = '__all__'