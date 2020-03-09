from django.shortcuts import render, get_object_or_404
from django.db.models import F
from .models import Ticket

# Create your views here.
def all_bugs(request):
    """
    Renders a page showing all the tickets with type bug and aren't completed
    """
    tickets = Ticket.objects.exclude(status='COMPLETED').filter(type='BUG')
    username = request.user.username
    return render(request, 'all_bugs.html', {'tickets': tickets}, username)

def all_features(request):
    """
    Renders a page showing all the tickets with type feature and aren't completed
    """
    tickets = Ticket.objects.exclude(status='COMPLETED').filter(type='FEATURE')
    return render(request, 'all_features.html', {'tickets': tickets})

def view_bug(request, id):
    """
    A view bug page with comments and also increments the views counter
    """
    bug = Ticket.objects.get(id=id)

    # View Incrementer
    bugViews = get_object_or_404(Ticket, pk=id)
    bugViews.views = F('views') + 1
    bugViews.save()

    return render(request, 'view_bug.html', {'bug': bug})
