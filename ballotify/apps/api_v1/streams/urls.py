from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.streams.views',

    url(r'^$', 'streams_view', name='streams'),
    url(r'^(?P<slug>[\w-]+)/$', 'stream_detail_view', name='stream-detail'),
    url(r'^(?P<slug>[\w-]+)/followers/$', 'stream_followers_view', name='stream-followers'),

    url(r'^(?P<slug>[\w-]+)/questions/$', 'stream_questions_view', name='stream-questions'),
    url(r'^(?P<slug>[\w-]+)/questions/(?P<question_slug>[\w-]+)/$', 'stream_question_detail_view', name='stream-question-detail'),
)
