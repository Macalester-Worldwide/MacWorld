from django.shortcuts import render
from Couches.models import Couch

def index(request):
    return render(request, 'index.html', {'couches' : Couch.objects.all()})