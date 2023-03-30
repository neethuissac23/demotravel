from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    obj=team.objects.all()
    placeobj=place.objects.all()
    return render(request, 'index.html',{'result':obj,'placeresult':placeobj})
