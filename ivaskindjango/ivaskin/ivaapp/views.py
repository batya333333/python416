from django.shortcuts import render
from .models import App

# Create your views here.
def ind(request):
    props = App.objects.all()
    return render(request,'ivaapp/index.html',{'props':props})