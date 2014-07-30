from Couches.models import User, Couch
from django.contrib.admin import site, TabularInline, ModelAdmin
from guardian.admin import GuardedModelAdmin


class CouchesProfileAdmin(GuardedModelAdmin):
    pass


class CouchAdmin(GuardedModelAdmin):
    pass

site.register(User, CouchesProfileAdmin)
site.register(Couch, CouchAdmin)