from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Ticket
from comments.models import Comment
from .forms import TicketForm
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.
def all_bugs(request):
    """
    Renders a page showing all the tickets with type bug and aren't completed
    """
    tickets = Ticket.objects.exclude(status='COMPLETED').filter(type='BUG')
    username = request.user.username
    return render(request, 'all_bugs.html', {'tickets': tickets}, username)


def all_completed_bugs(request):
    """
    Renders a page showing all the tickets with type bug and aren't completed
    """
    tickets = Ticket.objects.filter(type='BUG',status='COMPLETED')
    username = request.user.username
    return render(request, 'all_completed_bugs.html', {'tickets': tickets}, username)


def all_features(request):
    """
    Renders a page showing all the tickets with type feature and aren't completed
    """
    tickets = Ticket.objects.exclude(status='COMPLETED').filter(type='FEATURE')
    return render(request, 'all_features.html', {'tickets': tickets})

def all_completed_features(request):
    """
    Renders a page showing all the tickets with type bug and aren't completed
    """
    tickets = Ticket.objects.filter(type='FEATURE',status='COMPLETED')
    username = request.user.username
    return render(request, 'all_completed_features.html', {'tickets': tickets}, username)

def view_ticket(request, id):
    """
    A view bug page with comments and also increments the views counter
    """
    ticket = Ticket.objects.get(id=id)

    try:
        comments = Comment.objects.filter(ticketID=id)
    except Comment.DoesNotExist:
        comments = None

    # View Incrementer
    ticketViews = get_object_or_404(Ticket, pk=id)
    ticketViews.views = F('views') + 1
    ticketViews.save()

    user = User.objects.get(email=request.user.email)
    
    return render(request, 'view_ticket.html', {'ticket': ticket,'comments': comments, 'user': user})

def create_or_edit_bug(request, pk=None):
    """
    Create a  view that allows us to crate
    or edit a ticket depending if the ticket ID
    is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    username = request.user.username
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.type = "BUG"
            ticket.author = username.capitalize()
            ticket.save()
            return redirect(view_ticket, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'bugform.html', {'form': form})


def create_or_edit_feature(request, pk=None):
    """
    Create a  view that allows us to create
    or edit a ticket depending if the ticket ID
    is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    username = request.user.username
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.type = "FEATURE"
            ticket.author = username.capitalize()
            ticket.save()
            return redirect(view_ticket, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'featureform.html', {'form': form})


def ticket_upvote(request, pk=None):
    """
    Upvote view for tickets
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    user = User.objects.get(email=request.user.email)
    ticket.upvotes = F('upvotes') + 1
    ticket.views = F('views') - 1
    user.profile.bug_upvotes += 1
    user.profile.save()
    ticket.save()
    return redirect(view_ticket, ticket.pk)

def feature_upvote(request, pk=None):
    """
    Upvote view for tickets
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    user = User.objects.get(email=request.user.email)
    if(user.profile.points_available >= 1):
        user.profile.points_available -= 1
        user.profile.feature_upvotes += 1
        user.profile.save()
        ticket.upvotes = F('upvotes') + 1
    ticket.views = F('views') - 1
    ticket.save()
    return redirect(view_ticket, ticket.pk)