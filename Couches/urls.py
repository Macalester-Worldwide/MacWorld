from Couches.api import CouchViewSet
from Couches.views import CouchesHomeView, CouchCreateView, CouchUpdateView, CouchDeleteView, CouchDetailView, ProfileUpdateView, ProfileDetailView, ProfileEmailFormView
from django.conf.urls import patterns, url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'couches', CouchViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                       url(r'^couch/create/$', CouchCreateView.as_view(), name='couch.create'),
                       url(r'^couch/(?P<pk>\d+)/edit/$', CouchUpdateView.as_view(), name='couch.update'),
                       url(r'^couch/(?P<pk>\d+)/delete/$', CouchDeleteView.as_view(), name='couch.delete'),
                       url(r'^couch/(?P<pk>\d+)/$', CouchDetailView.as_view(), name='couch.detail'),

                       url(r'^profile/(?P<username>\w+)/edit/$', ProfileUpdateView.as_view(), name='profile.update'),
                       url(r'^profile/(?P<username>\w+)/$', ProfileDetailView.as_view(), name='profile.detail'),
                       url(r'^profile/(?P<username>\w+)/email/$', ProfileEmailFormView.as_view(), name='profile.email'),
)