from django.conf.urls import patterns, include, url
from roster import views 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'roster.views.home', name='home'),
    url(r'^team/$', views.team, name='roster_team'),
    url(r'^player/$', views.player, name='roster_player'),
    # url(r'^Basketball/', include('Basketball.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^', include('roster.urls')), 
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
