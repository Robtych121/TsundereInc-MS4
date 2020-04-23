from django.conf.urls import url, include
from .views import create_or_edit_comment

urlpatterns = [
    url(r'^new-comment/(?P<id>\d+)', create_or_edit_comment, name='new_comment'),
]
