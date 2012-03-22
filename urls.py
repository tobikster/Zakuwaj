from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Examples:
# url(r'^$', 'Zakuwaj.views.home', name='home'),
# url(r'^Zakuwaj/', include('Zakuwaj.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
	url(r'^words/', include('words.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
