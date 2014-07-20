from Couches.views import HomeView, LoginView, LogoutView, ProfileDetailView, ProfileUpdateView, RegisterView, UserView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^user/(?P<username>.+)/$', UserView.as_view(), name='user-detail'),
    url(r'^register/$', RegisterView.as_view(), name='user-register'),
    url(r'^login/$', LoginView.as_view(), name='user-login'),
    url(r'^logout/$', LogoutView.as_view(), name='user-logout'),
    url(r'^profile/(?P<username>.+)/edit/$', ProfileUpdateView.as_view(), name='profile-update'),
    url(r'^profile/(?P<username>.+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^$', HomeView.as_view(), name='home'),
)

user_patterns = patterns('',
    url(r'$', UserView.as_view(), name='user-detail'),
)