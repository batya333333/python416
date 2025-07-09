from django.shortcuts import render
from .models import App

# Create your views here.
def page(request):
    project = App.objects.all()
    return render(request, 'dz/index.html',{'app' : project})
