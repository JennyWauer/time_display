from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.

def display(request):
    context = {
        "time": strftime("%B, %A, %y, %I, %M, %p")
    }
    return render(request, "index.html", context)