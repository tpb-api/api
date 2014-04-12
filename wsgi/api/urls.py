from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from torrents import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    url(r'^torrents/', include(urls)),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # url(r'^admin/', include(admin.site.urls)),
)
