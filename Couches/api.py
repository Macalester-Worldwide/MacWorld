from Couches.models import Couch
from Couches.serializers import CouchSerializer
from rest_framework.viewsets import ModelViewSet


class CouchViewSet(ModelViewSet):
    queryset = Couch.objects.all()
    serializer_class = CouchSerializer