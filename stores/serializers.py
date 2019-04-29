from rest_framework import serializers
from .models import Stores


class StoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stores
        fields= ('location', 'postcode', 'latitude', 'longitude')
