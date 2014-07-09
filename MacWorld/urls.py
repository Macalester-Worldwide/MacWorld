from django.conf.urls import patterns, include, url
from django.contrib import admin
from Couches.forms import SignupFormExtra

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    (r'^Couches/signup/$',
	'userena.views.signup',
	{'signup_form': SignupFormExtra}),
	(r'^Couches/', include('userena.urls')),
	(r'^messages/', include('userena.contrib.umessages.urls')),
)