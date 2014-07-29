from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

auth_urls = patterns('',
    url(r'^login/$', name='auth-login'),
    url(r'^logout/$', name='auth-logout'),
    url(r'^register/$', name='auth-register'),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^couches/', include('Couches.urls')),
    url(r'^auth/', include(auth_urls, namespace='auth'))
)