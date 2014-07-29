from Couches.models import CouchesProfile, Couch
from rest_framework.serializers import HyperlinkedModelSerializer


class CouchesProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CouchesProfile
        fields = ('user', 'description', 'contact_information', 'graduation_year')


class CouchSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Couch
        fields = ('user', 'longitude', 'latitude', 'address')