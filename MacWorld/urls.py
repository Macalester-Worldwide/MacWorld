from MacWorld.views import HomeView, AuthHomeView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('allauth.urls')),
    url(r'^auth/$', AuthHomeView.as_view(), name='auth.home'),
    url(r'^', include('Couches.urls', namespace='couches')),
    url(r'^$', HomeView.as_view(), name='home'),
)