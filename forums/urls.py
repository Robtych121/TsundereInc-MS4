from django.conf.urls import url, include
from .views import forums

urlpatterns = [
    url(r'^forums/$', forums, name='forums'),
]