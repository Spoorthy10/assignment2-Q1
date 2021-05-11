from django.shortcuts import render
import datetime
# Create your views here.

def sample1(request):
    date=datetime.datetime.now()
    return render(request, "page.html", {'dt':date})
