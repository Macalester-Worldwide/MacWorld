from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm
from userena.forms import EditProfileForm
from Couches.models import Location
from django.core.validators import RegexValidator

# Code adapted from: http://django-userena.readthedocs.org/en/latest/faq.html#how-do-i-add-extra-fields-to-forms
class SignupFormExtra(SignupForm):
	first_name = forms.CharField(label=_(u'First name'),
								 max_length=30,
								 required=True)
	last_name = forms.CharField(label=_(u'Last name'),
								max_length=30,
								required=True)
	latitude = forms.CharField(label=_(u'Latitude'),
								 max_length=30,
								 required=False)
	longitude = forms.CharField(label=_(u'Longitude'),
								 max_length=30,
								 required=False)

	def save(self):
		# First save the parent form and get the user.
		new_user = super(SignupFormExtra, self).save()
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.save()

		Location.objects.create(available=True, 
								user=new_user, 
								latitude=self.cleaned_data['latitude'], 
								longitude=self.cleaned_data['longitude'])
		

		return new_user

class EditProfileFormExtra(EditProfileForm):
	description = forms.CharField(label=_(u'Description'),
							      max_length=300,
							      required=True,
							      widget=forms.Textarea)
	contact_information = forms.CharField(label=_(u'Contact Information'),
							      max_length=300,
							      required=True,
							      widget=forms.Textarea)
	graduation_year = forms.CharField(label=_(u'Longitude'),
								 max_length=4,
								 required=False,
								 validators=[RegexValidator(regex='^\d{4}$'),])
	def save(self):
		profile = super(EditProfileFormExtra, self).save()
		profile.description = self.cleaned_data['description']
		profile.contact_information = self.cleaned_data['contact_information']
		profile.graduation_year = self.cleaned_data['graduation_year']
		return profile