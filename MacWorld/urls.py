from Couches.views import CouchDetail, CouchCreate, CouchUpdate, CouchDelete
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Couches.forms import SignupFormExtra
from Couches.forms import EditProfileFormExtra

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^Couches/signup/$', 'userena.views.signup',
                           {'template_name': 'signup.html', 'signup_form': SignupFormExtra}),
                       url(r'^Couches/(?P<username>[\.\w-]+)/edit/$', 'userena.views.profile_edit',
                           {'template_name': 'profile_form.html', 'edit_profile_form': EditProfileFormExtra}),
                       url(r'^Couches/(?P<username>[\.\w-]+)/$', 'userena.views.profile_detail',
                           {'template_name': 'profile_detail.html'}),
                       url(r'^Couches/', include('userena.urls')),
                       url(r'^messages/', include('userena.contrib.umessages.urls')),
                       url(r'^couch_detail/(?P<pk>\d+)/$', CouchDetail.as_view(), name='couches-couch-detail'),
                       url(r'^couch_delete/(?P<pk>\d+)/$', CouchDelete.as_view(), name='couches-couch-delete'),
                       url(r'^couch_update/(?P<pk>\d+)/$', CouchUpdate.as_view(), name='couches-couch-update'),
                       url(r'^couch_create/$', CouchCreate.as_view(), name='couches-couch-create'),
)