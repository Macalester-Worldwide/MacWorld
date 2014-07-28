from Couches.models import UserProfile, Couch
from rest_framework.serializers import HyperlinkedModelSerializer


class CouchesProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'description', 'contact_information', 'graduation_year')


class CouchSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Couch
        fields = ('user', 'longitude', 'latitude', 'address')