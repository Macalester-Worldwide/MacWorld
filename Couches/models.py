from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.core.validators import RegexValidator


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')

    first_name = models.TextField()
    last_name = models.TextField()
    description = models.CharField(max_length=300, blank=True)
    contact_information = models.CharField(max_length=300, blank=True) # extra contact information that the user wishes to include
    graduation_year = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Location(models.Model):
    user = models.ForeignKey(User, related_name="locations")
    available = models.BooleanField(default=True) # Is this location available to couchsurf
    
    latitude = models.CharField(max_length=30, validators=[RegexValidator(regex='^[-+]?[0-9]*\.?[0-9]+$'),]) # floating point validator
    longitude = models.CharField(max_length=30, validators=[RegexValidator(regex='^[-+]?[0-9]*\.?[0-9]+$'),]) # floating point validator
    address = models.CharField(max_length=100, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)