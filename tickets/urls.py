from django.conf.urls import url, include
from .views import all_tickets

urlpatterns = [
    url(r'^$', all_tickets, name='all_tickets')
]