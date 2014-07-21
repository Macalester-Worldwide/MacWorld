from django.db.models import Model, OneToOneField, IntegerField, TextField, ForeignKey, FloatField, CharField
from django.contrib.auth.models import User


class CouchesProfile(Model):
    user = OneToOneField(User, related_name='profile')
    description = TextField(max_length=300, blank=True)
    contact_information = TextField(max_length=300, blank=True)
    graduation_year = IntegerField(null=True, blank=True)

    def get_full_name(self):
        return self.user.get_full_name()

    def __unicode__(self):
        return unicode(self.user.get_full_name())


class Couch(Model):
    class Meta:
        verbose_name_plural = 'couches'
    owner = ForeignKey(CouchesProfile, related_name='couches')
    lon = FloatField()
    lat = FloatField()

    def __unicode__(self):
        return unicode('Couch owned by %s at (%s, %s)' % (self.owner, self.lat, self.lon))