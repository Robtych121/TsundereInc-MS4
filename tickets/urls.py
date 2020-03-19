from django.conf.urls import url, include
from .views import all_bugs, all_completed_bugs, all_features, all_completed_features , view_ticket, create_or_edit_bug, create_or_edit_feature, ticket_upvote, feature_upvote

urlpatterns = [
    url(r'^bugs/$', all_bugs, name='all_bugs'),
    url(r'^bugs-completed/$', all_completed_bugs, name='all_completed_bugs'),
    url(r'^features/$', all_features, name='all_features'),
    url(r'^features-completed/$', all_completed_features, name='all_completed_features'),
    url(r'^view-ticket/(?P<id>\d+)', view_ticket, name='view_ticket'),
    url(r'^new-bug/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit-bug/$', create_or_edit_bug, name='edit_bug'),
    url(r'^new-feature/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit-feature/$', create_or_edit_feature, name='edit_feature'),
    url(r'^(?P<pk>\d+)/bug-upvote/$', ticket_upvote, name='ticket_upvote'),
    url(r'^(?P<pk>\d+)/feature-upvote/$', feature_upvote, name='feature_upvote')
]