from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',

    url(r'^user/', include('api_v1.user.urls', namespace='user')),
    url(r'^streams/', include('api_v1.streams.urls', namespace='streams')),
    url(r'^questions/', include('api_v1.questions.urls', namespace='questions')),
    url(r'^accounts/', include('api_v1.accounts.urls', namespace='accounts')),
    url(r'^', include('api_v1.auth.urls', namespace='auth')),
)
