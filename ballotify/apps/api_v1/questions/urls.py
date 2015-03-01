from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.questions.views',

    url(r'^$', 'questions_view', name='questions'),
    url(r'^(?P<slug>[\w-]+)/$', 'question_detail_view', name='question-detail'),
)
