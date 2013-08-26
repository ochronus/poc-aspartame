from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'aspartame.views.home', name='home'),
    url(r'^redirect/index/$', 'aspartame.views.redirect_container', name='redirect_container'),
    url(r'^redirect/$', 'aspartame.views.redirect', name='redirect'),
    url(r'^redirect/(?P<id>[\w-]+)/$', 'aspartame.views.redirect', name='redirect'),
)
