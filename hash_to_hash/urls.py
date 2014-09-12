from django.conf.urls import *


urlpatterns = patterns('hash_to_hash.views',
                       url(r'^consent/$', 'load_consent'),
                       url(r'^start/$', 'load_start'),
                       url(r'^$', 'load_consent'),
                       url(r'^survey/$', 'load_survey'))
