from MacWorld import settings
from MacWorld.views import HomeView
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('allauth.urls')),
    url(r'^', include('Couches.urls', namespace='couches')),
    url(r'^$', HomeView.as_view(), name='home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)