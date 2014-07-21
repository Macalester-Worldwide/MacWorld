from Couches.views import ProfileUpdateView, ProfileDetailView, CouchesHomeView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<username>.+)/edit/$', ProfileUpdateView.as_view(), name='couches-profile-update'),
    url(r'^(?P<username>.+)/$', ProfileDetailView.as_view(), name='couches-profile-detail'),
    url(r'^$', CouchesHomeView.as_view(), name='couches-home')
)