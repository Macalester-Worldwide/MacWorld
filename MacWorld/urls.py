from MacWorld.views import HomeView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('allauth.urls')),
    url(r'^', include('Couches.urls', namespace='couches')),
    url(r'^$', HomeView.as_view(), name='home'),
)