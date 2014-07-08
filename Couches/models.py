from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.core.validators import validate_email
from django.core.validators import RegexValidator


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, validators=[validate_email])
    description = models.CharField(max_length=300)
    picture = models.FileField(upload_to='.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Location(models.Model):
	user = models.ForeignKey(UserProfile)
	available = models.BooleanField() # Is this location available to couchsurf?
	latitude = models.CharField(max_length=30, validators=[RegexValidator(regex='^[-+]?[0-9]*\.?[0-9]+$'),]) # floating point validator
	longitude = models.CharField(max_length=30, validators=[RegexValidator(regex='^[-+]?[0-9]*\.?[0-9]+$'),]) # floating point validator