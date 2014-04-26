from django.db import models
from rest_framework import viewsets
# Torrent API
from tpb import TPB
from tpb import CATEGORIES, ORDERS
from api.torrents.serializers import TorrentSerializer

t = TPB('https://thepiratebay.se')

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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

        return torrents_query

    serializer_class = TorrentSerializer
