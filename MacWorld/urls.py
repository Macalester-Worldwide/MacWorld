from Couches.views import LocationUpdate, LocationCreate, LocationDelete
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Couches.forms import SignupFormExtra
from Couches.forms import EditProfileFormExtra

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^Couches/signup/$',
    'userena.views.signup',
    {'template_name':'signup.html','signup_form': SignupFormExtra}),
    url(r'^Couches/(?P<username>[\.\w-]+)/edit/$',
    'userena.views.profile_edit',
    {'template_name':'profile_form.html','edit_profile_form': EditProfileFormExtra}),
    url(r'^Couches/(?P<username>[\.\w-]+)/$',
    'userena.views.profile_detail',
    {'template_name':'profile_detail.html'}),
    url(r'^Couches/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^location_delete/(?P<pk>\d+)/$', LocationDelete.as_view(), name='couches-location-delete'),
    url(r'^location_update/(?P<pk>\d+)/$', LocationUpdate.as_view(), name='couches-location-update'),
    url(r'^location_create/$', LocationCreate.as_view(), name='couches-location-create'),
)