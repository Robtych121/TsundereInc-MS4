from django.shortcuts import render
from .models import Ticket

# Create your views here.
def all_bugs(request):
    tickets = Ticket.objects.filter(type='BUG')
    return render(request, 'all_bugs.html', {'tickets': tickets})

def all_features(request):
    tickets = Ticket.objects.filter(type='FEATURE')
    return render(request, 'all_features.html', {'tickets': tickets})