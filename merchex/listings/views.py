from django.shortcuts import render
from .models import Band

# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands' : bands})