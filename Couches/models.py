from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, FloatField, CharField, DateTimeField, ImageField, IntegerField
from django.db.models.fields import EmailField, BooleanField
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import assign_perm


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', ]
    COLLEGE_FOUNDED_YEAR = 1874
    GRADUATION_YEAR_CHOICES = reversed(tuple([(i, i) for i in range(COLLEGE_FOUNDED_YEAR, datetime.now().year + 6)]))

    objects = UserManager()
    username = CharField(unique=True, max_length=30)
    email = EmailField(unique=True)
    name = CharField(_('full name'), max_length=100, blank=True)
    email_visible = BooleanField(_('Email visibility'), 
                    default=False, help_text=_('Enabiling this allows other users to see your e-mail.'))
    is_staff = BooleanField(_('staff status'), default=False,
                            help_text=_('Designates whether the user can log into this admin site.'))
    is_active = BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = DateTimeField(_('date joined'), auto_now_add=True)

    profile_picture = ImageField(_('picture of user'), null=True, blank=True, upload_to='Couches/static/profile_pictures/')
    contact_information = CharField(max_length=300, help_text=_('How can others contact you?'))
    description = CharField(max_length=500, help_text=_('Tell us a bit more about yourself.'))
    graduation_year = IntegerField(null=True, choices=GRADUATION_YEAR_CHOICES)

    def save(self, *args, **kwargs):  # FIXME: This should only be done on user creation
        super(User, self).save()
        if not ObjectPermissionChecker(self).has_perm('Couches.change_user', self):
            assign_perm('Couches.change_user', self, self)

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
    address = CharField(max_length=200, help_text=_('Where are you located? You can type your full address or only city you are located in.'))
    formatted_address = CharField(max_length=200, help_text=_('The address as formatted by google maps geolocation.'))
    description = CharField(max_length=150, blank=True, help_text=_('A description of this couch. How many people can you host? Is it a futon or a sofa?'))

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('couches:couch.detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return unicode('Couch owned by %s at (%s, %s)' % (self.owner, self.latitude, self.longitude))