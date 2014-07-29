from MacWorld.views import LoginView, LogoutView, RegisterView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

auth_urls = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^change_password', name='change_password'),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(auth_urls, namespace='auth')),
    url(r'^couches/', include('Couches.urls')),
)