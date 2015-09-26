from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from hacker.models import Hacker
from hacker.serializers import HackerSerializer

# Create your views here.


class HackerViewSet(viewsets.ModelViewSet):
    queryset = Hacker.objects.all()
    serializer_class = HackerSerializer
