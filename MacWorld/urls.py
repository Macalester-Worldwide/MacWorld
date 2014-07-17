from Couches.views import LoginView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^$', HomeView.as_view(), name='home')
)