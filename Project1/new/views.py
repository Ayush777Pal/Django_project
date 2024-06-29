from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request, "new/index.html",{
        "date":now.day==1 and now.month==1
    })
