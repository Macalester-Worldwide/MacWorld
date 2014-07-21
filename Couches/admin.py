from Couches.models import CouchesProfile, Couch
from django.contrib.admin import site, TabularInline, ModelAdmin


class CouchInline(TabularInline):
    model = Couch


class CouchesProfileAdmin(ModelAdmin):
    inlines = [
        CouchInline,
    ]

site.register(CouchesProfile, CouchesProfileAdmin)
site.register(Couch)