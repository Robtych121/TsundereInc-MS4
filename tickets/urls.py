from django.conf.urls import url, include
from .views import all_bugs, all_features, view_bug

urlpatterns = [
    url(r'^bugs/$', all_bugs, name='all_bugs'),
    url(r'^tickets/$', all_features, name='all_features'),
    url(r'^view-bug/(?P<id>\d+)', view_bug, name='view_bug'),
]