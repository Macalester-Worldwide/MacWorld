from Couches.models import Couch, UserProfile
from Couches.serializers import CouchSerializer, CouchesProfileSerializer
from rest_framework.viewsets import ModelViewSet


class CouchViewSet(ModelViewSet):
    queryset = Couch.objects.all()
    serializer_class = CouchSerializer


class CouchesProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CouchesProfileSerializer