from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api.torrents.views import TorrentViewSet

torrent_list = TorrentViewSet.as_view({
    'get': 'list'
})
torrent_detail = TorrentViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = patterns('api.torrents.views',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', torrent_list, name='torrent-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
