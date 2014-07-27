from MacWorld.views import HomeView, LoginView, LogoutView, UserCreateView, UserDetailView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Couches import urls as couches_urls

admin.autodiscover()

user_patterns = patterns('',
    url(r'^register/$', UserCreateView.as_view(), name='user-create'),
    url(r'^login/$', LoginView.as_view(), name='user-login'),
    url(r'^logout/$', LogoutView.as_view(), name='user-logout'),
    url(r'(?P<username>.+)/$', UserDetailView.as_view(), name='user-detail')
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^auth/', include(user_patterns), name='user'),
    url(r'^couches/', include(couches_urls), name='couches'),
    url(r'^$', HomeView.as_view(), name='home'),
)