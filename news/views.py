from django.shortcuts import render, get_object_or_404
from.models import Articolo, Giornalista
#Create your views here.
def home (request):...


def articoloDetailView(request, pk):
# articolo Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render (request, "articolo_detail.html", context)

def listaArticoli (request, pk=None):
    if pk==None:
        articoli=Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context ={
        'articoli': articoli,
        'pk': pk,
        }
    return render(request, 'lista_articoli.html', context)