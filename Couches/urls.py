from Couches.views import ProfileUpdateView, ProfileDetailView, CouchesHomeView, ProfileCreateView, CouchCreateView, \
    CouchUpdateView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^create_profile/$', ProfileCreateView.as_view(), name='couches-profile-create'),
    url(r'^create_couch/$', CouchCreateView.as_view(), name='couches-couch-create'),
    url(r'^edit_couch/(?P<pk>\d+)/$', CouchUpdateView.as_view(), name='couches-couch-update'),
    url(r'^(?P<username>.+)/edit/$', ProfileUpdateView.as_view(), name='couches-profile-update'),
    url(r'^(?P<username>.+)/$', ProfileDetailView.as_view(), name='couches-profile-detail'),
    url(r'^$', CouchesHomeView.as_view(), name='couches-home')
)