from .models import ScoresModel
from rest_framework import serializers


# Serializers define the API representation.
class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScoresModel
        fields = ('score',)
