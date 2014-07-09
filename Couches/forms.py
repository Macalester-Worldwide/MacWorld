from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm

# Code adapted from: http://django-userena.readthedocs.org/en/latest/faq.html#how-do-i-add-extra-fields-to-forms
class SignupFormExtra(SignupForm):
	first_name = forms.CharField(label=_(u'First name'),
								 max_length=30,
								 required=True)
	last_name = forms.CharField(label=_(u'Last name'),
								max_length=30,
								required=True)
	primary_location = forms.CharField(label=_(u'Host location'),
								max_length=30,
								required=True)
	description = forms.CharField(label=_(u'Description'),
								 max_length=300,
								 required=False)
	contact_information = forms.CharField(label=_(u'Description'),
								 max_length=300,
								 required=False)
	latitude = forms.CharField(label=_(u'Latitude'),
								 max_length=30,
								 required=False)
	longitude = forms.CharField(label=_(u'Longitude'),
								 max_length=30,
								 required=False)

	def __init__(self, *args, **kw):
		super(SignupFormExtra, self).__init__(*args, **kw)
		# Put the first and last name at the top
		new_order = self.fields.keyOrder[:-2]
		new_order.insert(0, 'first_name')
		new_order.insert(1, 'last_name')
		self.fields.keyOrder = new_order

	def save(self):
		# First save the parent form and get the user.
		new_user = super(SignupFormExtra, self).save()
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.description = self.cleaned_data['description']
		new_user.contact_information = self.cleaned_data['contact_information']
		new_user.save()

		user_location = Location()
		user_location.available = True
		user_location.user = new_user
		user_location.latitude = self.cleaned_data['latitude']
		user_location.longitude = self.cleaned_data['longitude']

		return new_user