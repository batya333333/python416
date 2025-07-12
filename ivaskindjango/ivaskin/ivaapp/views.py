from django.shortcuts import render, get_object_or_404
from .models import App, Forclient


# Create your views here.
def ind(request):
    props = App.objects.all()
    clients = Forclient.objects.all()
    return render(request, 'ivaapp/index.html', {'props': props, 'clients': clients})


def desc(request, description_id):
    desc = get_object_or_404(Forclient, pk=description_id)
    # proc = Forclient.objects.all
    return render(request, 'ivaapp/description.html', {'desc': desc})
