from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',

    url(r'^accounts/', include('api_v1.accounts.urls', namespace='accounts')),
)
