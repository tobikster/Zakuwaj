﻿from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
	url(r'^words/', include('words.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^login$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
	url(r'^$', 'views.index'),
)
