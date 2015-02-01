from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.accounts.views',

    url(r'^(?P<username>[\w-]+)/$', 'account_detail_view', name='account-detail'),
    url(r'^(?P<username>[\w-]+)/streams/$', 'account_streams_view', name='account-streams'),
    url(r'^(?P<username>[\w-]+)/streams/(?P<slug>[\w-]+)/$', 'account_stream_detail_view', name='account-stream-detail'),
)
