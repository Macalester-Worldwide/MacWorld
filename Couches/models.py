from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, OneToOneField, IntegerField, TextField, ForeignKey, FloatField, CharField
from django.contrib.auth.models import User


class CouchesProfile(Model):
    user = OneToOneField(User, related_name='couches_profile')
    description = TextField(max_length=300, blank=True)
    contact_information = TextField(max_length=300, blank=True)
    graduation_year = IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('couches-profile-detail', kwargs={'username': self.user.username})

    def get_full_name(self):
        return self.user.get_full_name()

    def __unicode__(self):
        full_name = self.user.get_full_name()
        return unicode(full_name if full_name else self.user.username)


class Couch(Model):
    class Meta:
        verbose_name_plural = 'couches'
    owner = ForeignKey(CouchesProfile, related_name='couches')
    longitude = FloatField()
    latitude = FloatField()
    address = CharField(max_length=200)

    def get_absolute_url(self):
        return reverse_lazy('couches-profile-detail', kwargs={'username': self.owner.user.username})

    def __unicode__(self):
        return unicode('Couch owned by %s at (%s, %s)' % (self.owner, self.latitude, self.longitude))