from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.

def display(request):
    context = {
        "date": strftime("%A, %B %d, %Y%I:%M %p"),
        "time": strftime("%Y%I:%M %p")
    }
    return render(request, "index.html", context)