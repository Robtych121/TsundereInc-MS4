from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from tickets.views import view_bug

# Create your views here.
def create_or_edit_comment(request, id):
    """
    Create a  view that allows us to create
    or edit a comment depending if the comment ID
    is null or not
    """
    
    username = request.user.username
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = username.capitalize()
            comment.ticketID = id
            comment.save()
            return redirect(view_bug, id)
    else:
        form = CommentForm
    return render(request, 'commentform.html', {'form': form})