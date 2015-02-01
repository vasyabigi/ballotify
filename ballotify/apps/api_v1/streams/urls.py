from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.streams.views',

    url(r'^$', 'streams_view', name='streams'),
    url(r'^(?P<slug>[\w-]+)/$', 'stream_detail_view', name='stream-detail'),
    url(r'^(?P<slug>[\w-]+)/followers/$', 'stream_followers_view', name='stream-followers'),
)
