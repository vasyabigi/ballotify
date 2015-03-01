from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.questions.views',

    url(r'^$', 'questions_view', name='questions'),
    url(r'^(?P<slug>[\w-]+)/$', 'question_detail_view', name='question-detail'),
    url(r'^(?P<slug>[\w-]+)/choices/$', 'choices_view', name='question-choices'),
    url(r'^(?P<slug>[\w-]+)/votes/$', 'votes_view', name='question-votes'),
)
