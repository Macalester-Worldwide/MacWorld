from Couches.views import ProfileUpdateView, ProfileDetailView, CouchesHomeView, ProfileCreateView, CouchCreateView, \
    CouchUpdateView, CouchDeleteView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^couch/create$', CouchCreateView.as_view(), name='couches-couch-create'),
    url(r'^couch/(?P<pk>\d+)/edit/$', CouchUpdateView.as_view(), name='couches-couch-update'),
    url(r'^couch/(?P<pk>\d+)/delete/$', CouchDeleteView.as_view(), name='couches-couch-delete'),
    url(r'^profile/create/$', ProfileCreateView.as_view(), name='couches-profile-create'),
    url(r'^profile/(?P<username>.+)/edit/$', ProfileUpdateView.as_view(), name='couches-profile-update'),
    url(r'^profile/(?P<username>.+)/$', ProfileDetailView.as_view(), name='couches-profile-detail'),
    url(r'^$', CouchesHomeView.as_view(), name='couches-home'),
)