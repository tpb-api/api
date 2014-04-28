from django.forms import widgets
from rest_framework import serializers
from tpb import CATEGORIES
    
class TorrentSerializer(serializers.Serializer):
    id = serializers.Field() #Note:`Field` is an untyped read-only field.
    imdb_id = serializers.Field() #Note:`Field` is an untyped read-only field.
    clean_title = serializers.Field()
    year = serializers.Field()
    quality = serializers.Field()

    title = serializers.CharField(required=True,
                                  max_length=100)
    url = serializers.CharField(required=True,
                                 max_length=1000)
    category = serializers.CharField(required=False,
                                 max_length=1000)
    sub_category = serializers.CharField(required=False,
                                 max_length=1000)
    magnet_link = serializers.CharField(required=True,
                                 max_length=1000)
    torrent_link = serializers.CharField(required=True,
                                 max_length=1000)
    seeders = serializers.Field()
    leechers = serializers.Field()
