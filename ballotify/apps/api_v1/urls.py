from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',

    url(r'^user/', include('api_v1.user.urls', namespace='user')),
    url(r'^', include('api_v1.auth.urls', namespace='auth')),
)
