from django.conf.urls import url, include
from .views import all_bugs, all_features

urlpatterns = [
    url(r'^bugs/$', all_bugs, name='all_bugs'),
    url(r'^tickets/$', all_features, name='all_features')
]