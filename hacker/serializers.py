from hacker.models import Hacker
from rest_framework import serializers


class HackerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hacker
        fields = 'name', 'active', 'created'
