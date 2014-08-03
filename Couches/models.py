from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, BaseUserManager
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, FloatField, CharField, DateTimeField, ImageField, IntegerField
from django.db.models.fields import EmailField, BooleanField
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', ]
    COLLEGE_FOUNDED_YEAR = 1874
    GRADUATION_YEAR_CHOICES = reversed(tuple([(i, i) for i in range(COLLEGE_FOUNDED_YEAR, datetime.now().year + 6)]))

    objects = UserManager()
    username = CharField(unique=True, max_length=30)
    email = EmailField(unique=True)
    name = CharField(_('full name'), max_length=100, blank=True)
    email_visible = BooleanField(_('visibility of email towards other members'), 
                    default=False, help_text=_('Enabiling this allows other users to see your e-mail.'))
    is_staff = BooleanField(_('staff status'), default=False,
                            help_text=_('Designates whether the user can log into this admin site.'))
    is_active = BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = DateTimeField(_('date joined'), auto_now_add=True)

    profile_picture = ImageField(_('picture of user'), null=True, blank=True, upload_to='profile_pictures/')
    contact_information = CharField(max_length=300)
    description = CharField(max_length=500)
    graduation_year = IntegerField(null=True, choices=GRADUATION_YEAR_CHOICES)

    def get_full_name(self):
        return self.name

    def get_best_identifier(self):
        return self.name if self.name else self.username

    def get_absolute_url(self):
        return reverse_lazy('couches:profile.detail', kwargs={'username': self.username})


class Couch(Model):
    class Meta:
        verbose_name_plural = 'couches'

    owner = ForeignKey(User, related_name='couches')
    longitude = FloatField()
    latitude = FloatField()
    address = CharField(max_length=200, help_text=_('Type the address of your new location.'))
    formatted_address = CharField(max_length=200, help_text=_('The address as formatted by google maps geolocation.'))

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('couches:couch.detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return unicode('Couch owned by %s at (%s, %s)' % (self.owner, self.latitude, self.longitude))