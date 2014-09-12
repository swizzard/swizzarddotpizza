from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import main, load_cv, load_etc
# VERSION = 'production'
# handler404 = 'ffy.views.error_404'
# handler500 = 'ffy.views.error_500'
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', main),
    url(r'^load_cv/$', load_cv),
    url(r'^load_etc/$', load_etc),
    url(r'^cv/$', main),
    url(r'^about/$', main),
    url(r'^etc/$', main),
    url(r'^survey/$', main),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'hash/', include('hash_to_hash.urls')),
    url(r'ffy/', include('ffy.urls')),
    #url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    )

urlpatterns += staticfiles_urlpatterns()

# urlpatterns += patterns('django.contrib.flatpages.views',
# url(r'^$', 'flatpage', {'url':'/test/'}, name='test'),
# url(r'^cv/$', 'flatpage', {'url':'/cv/'}, name='cv'),
# url(r'^else/$', 'flatpage', {'url':'/else/'}, name='else'),
# )

