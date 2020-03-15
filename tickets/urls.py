from django.conf.urls import url, include
from .views import all_bugs, all_features, view_bug, create_or_edit_bug, ticket_upvote

urlpatterns = [
    url(r'^bugs/$', all_bugs, name='all_bugs'),
    url(r'^tickets/$', all_features, name='all_features'),
    url(r'^view-bug/(?P<id>\d+)', view_bug, name='view_bug'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/upvote/$', ticket_upvote, name='ticket_upvote')
]