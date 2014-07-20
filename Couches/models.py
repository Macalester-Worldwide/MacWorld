from django.db.models import Model, OneToOneField, IntegerField, TextField, ForeignKey, FloatField
from django.contrib.auth.models import User


class UserProfile(Model):
    user = OneToOneField(User, related_name='profile')
    description = TextField(max_length=300, blank=True)
    contact_information = TextField(max_length=300, blank=True)
    graduation_year = IntegerField(null=True, blank=True)

    def get_full_name(self):
        return self.user.get_full_name()

    def get_best_couch(self):
        return self.couches.all()[0]  # TODO: find a better way to pick top couch

    def __unicode__(self):
        return unicode(self.user.get_full_name())


class Couch(Model):
    class Meta:
        verbose_name_plural = 'couches'
    owner = ForeignKey(UserProfile, related_name='couches')
    lon = FloatField()
    lat = FloatField()