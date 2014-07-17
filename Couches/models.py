from django.db.models import Model, OneToOneField, IntegerField, TextField, ForeignKey, FloatField
from django.contrib.auth.models import User


class UserProfile(Model):
    user = OneToOneField(User, related_name='profile')
    description = TextField(max_length=300, blank=True)
    contact_information = TextField(max_length=300, blank=True)
    graduation_year = IntegerField(null=True, blank=True)

    def get_full_name(self):
        self.user.get_full_name()

    def __unicode__(self):
        return unicode(self.get_full_name())


class Couch(Model):
    owner = ForeignKey(UserProfile, related_name='couches')
    lon = FloatField()
    lat = FloatField()