from django.shortcuts import render

# Create your views here.
def index(request):
    """ Return the index.html """
    return render(request, "homepage.html")