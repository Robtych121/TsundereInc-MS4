from django.conf.urls import url, include
from .views import all_bugs, all_completed_bugs, all_features, view_ticket, create_or_edit_bug, ticket_upvote

urlpatterns = [
    url(r'^bugs/$', all_bugs, name='all_bugs'),
    url(r'^bugs-completed/$', all_completed_bugs, name='all_completed_bugs'),
    url(r'^tickets/$', all_features, name='all_features'),
    url(r'^view-ticket/(?P<id>\d+)', view_ticket, name='view_ticket'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/upvote/$', ticket_upvote, name='ticket_upvote')
]