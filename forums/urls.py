from django.conf.urls import url, include
from .views import forums, view_forum, create_or_edit_forum, forum_upvote, create_or_edit_forumcomment

urlpatterns = [
    url(r'^$', forums, name='forums'),
    url(r'^view/(?P<id>\d+)', view_forum, name='view_forum'),
    url(r'^new/$', create_or_edit_forum, name='new_forum'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_forum, name='edit_forum'),
    url(r'^(?P<pk>\d+)/upvote/$', forum_upvote, name='forum_upvote'),
    url(r'^new-comment/(?P<id>\d+)', create_or_edit_forumcomment, name='new_forumcomment'),
]