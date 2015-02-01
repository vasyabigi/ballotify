from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.user.views',

    url(r'^$', 'user_detail_view', name='user-detail'),
    url(r'^streams/$', 'user_streams_view', name='user-streams'),
)
