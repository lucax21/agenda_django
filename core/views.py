from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def eventos(request, titulo_evento):
    try:
        e = Evento.objects.get(titulo=titulo_evento)
        return HttpResponse('{}'.format(e.descricao))
    except:
        return HttpResponse('Não encontrado')

def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    response = {'evento':evento}
    return render(request, 'agenda.html', response)
