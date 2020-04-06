from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.

def do_search(request):
    tickets = Ticket.objects.filter(name__icontains=request.GET['q'])
    query = request.GET['q']
    return render(request, "search.html", {'tickets': tickets, 'query': query})