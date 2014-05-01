from django.db import models
from rest_framework import viewsets
# Torrent API
from tpb import TPB
from tpb import CATEGORIES, ORDERS
from api.torrents.serializers import TorrentSerializer
import urllib.request
import json
import re

t = TPB('https://thepiratebay.se')
imdb_api ="http://shothere.geniusweb.fr/search/imdb_movies.json?q="
class ImdbMovie(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title
def object_decoder(obj):
    return ImdbMovie(obj['id'], obj['title'])

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Torrent(object):
    def __init__(self, tpb_torrent):
        self.id = tpb_torrent.id
        self.title = tpb_torrent.title
        self.url = tpb_torrent.url
        self.category = tpb_torrent.category
        self.sub_category = tpb_torrent.sub_category
        self.magnet_link = tpb_torrent.magnet_link
        self.torrent_link = tpb_torrent.torrent_link
        self.seeders = tpb_torrent.seeders
        self.leechers = tpb_torrent.leechers
        self.clean_title = self.title
        self.imdb_id = 0
        self.year = 0
        self.quality = 0
        self.set_imdb_data()

    def set_imdb_data(self):
        md = re.match( r'(.+?)\(?([0-9]{4})\)?.+', self.title, re.M|re.I)
        if md:
            self.clean_title = md.group(1)
            self.year = md.group(2)
        else:
            self.clean_title = self.title
        md = re.match( r'(720p|1080p)', self.title, re.M|re.I)
        if md:
            self.quality = md.group(1)

        query_url = u''.join([imdb_api,self.clean_title])
        response = urllib.request.urlopen(query_url)
        resp_parsed = json.loads(response.read().decode("utf-8"), object_hook=object_decoder)
        if resp_parsed:
            self.clean_title = resp_parsed[0].title
            self.imdb_id = u''.join(['tt',resp_parsed[0].id])

class TorrentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        keywords = self.request.QUERY_PARAMS.get('keywords', '')
        category = self.request.QUERY_PARAMS.get('category', 'HD_MOVIES')

        torrents_query = t.search(keywords, category=getattr(CATEGORIES.VIDEO, category))

        sort = self.request.QUERY_PARAMS.get('sort', None)
        if sort is not None:
            if sort == 'seeds':
                torrents_query = torrents_query.order(ORDERS.SEEDERS.ASC)
            elif sort == 'name':
                torrents_query = torrents_query.order(ORDERS.NAME.ASC)
            else:
                torrents_query = torrents_query.order(ORDERS.SEEDERS.ASC)

        page = self.request.QUERY_PARAMS.get('page', None)
        if page is not None:
            torrents_query =  torrents_query.page(page)
    
        #adding this fixed the _clone missing error
        def clone(self):
        #return self  - this works as well.
            return self

        torrents_query.__class__._clone = clone
        #end of addition
        
        query_s = []
        for torrent in torrents_query:
            query_s.append(Torrent(torrent))
        return query_s

    serializer_class = TorrentSerializer
