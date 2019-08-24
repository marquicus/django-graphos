from django.conf.urls import include, url
from django.conf import settings


urlpatterns = [
    url(r'^', include("demo.urls")),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
]
