from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^', include('rest_framework_swagger.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include('api_v1.urls')),
)
