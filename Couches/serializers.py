from Couches.models import Couch
from rest_framework.serializers import HyperlinkedModelSerializer


class CouchSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Couch
        fields = ('user', 'longitude', 'latitude', 'address')