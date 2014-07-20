from Couches.models import UserProfile
from django.forms import ModelForm


class ProfileForm(ModelForm):  # form for creating or editing user profile
    class Meta:
        model = UserProfile
        fields = ['user', 'description', 'contact_information', 'graduation_year']