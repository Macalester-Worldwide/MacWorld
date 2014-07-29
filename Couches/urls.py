from Couches.api import CouchViewSet, CouchesProfileViewSet
from Couches.views import ProfileUpdateView, ProfileDetailView, CouchesHomeView, ProfileCreateView, CouchCreateView, \
    CouchUpdateView, CouchDeleteView
from django.conf.urls import patterns, url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'couches', CouchViewSet)
router.register(r'couchesprofiles', CouchesProfileViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^couch/create$', CouchCreateView.as_view(), name='couch-create'),
    url(r'^couch/(?P<pk>\d+)/edit/$', CouchUpdateView.as_view(), name='couch-update'),
    url(r'^couch/(?P<pk>\d+)/delete/$', CouchDeleteView.as_view(), name='couch-delete'),
    url(r'^profile/create/$', ProfileCreateView.as_view(), name='profile-create'),
    url(r'^profile/(?P<username>.+)/edit/$', ProfileUpdateView.as_view(), name='profile-update'),
    url(r'^profile/(?P<username>.+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^$', CouchesHomeView.as_view(), name='home'),
)