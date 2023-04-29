from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DefaultModel

from .serializers import DefaultSerializer

# Create your views here.


class DefaultViewSet(ModelViewSet):
    serializer_class = DefaultSerializer
    queryset = DefaultModel.objects.all()

