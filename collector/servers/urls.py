from django.conf.urls import patterns, include, url
from .views import ServerDataFetchView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'collector.servers.views.IndexView', name='home'),
    # url(r'^collector/', include('collector.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^/', include('collector.server.urls')),
	url(r'^(?P<server_id>\w+-\w+-\w+-\w+)/(?P<action>\w+)',  ServerDataFetchView),
)
