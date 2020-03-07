from django.shortcuts import render
from .models import Ticket

# Create your views here.
def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'all_tickets.html', {'tickets': tickets})