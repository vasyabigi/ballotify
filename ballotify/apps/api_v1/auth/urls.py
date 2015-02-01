from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api_v1.auth.views',

    url(r'^login/$', 'login_view', name='login'),
)
