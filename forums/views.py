from django.shortcuts import render
from .models import Forum

# Create your views here.
def forums(request):
    """
    Renders a page showing all the forums
    """
    forums = Forum.objects.all()
    username = request.user.username
    return render(request, 'forums.html', {'forums': forums}, username)