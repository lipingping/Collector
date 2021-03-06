from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collector.views.home', name='home'),
    # url(r'^collector/', include('collector.foo.urls')),
    url(r'^tools/', 'collector.tools.views.IndexView', name='ToolsHome'),
    url(r'^docs/', 'collector.tools.views.IndexView', name='ToolsHome'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^servers/', include('collector.servers.urls')),
)
