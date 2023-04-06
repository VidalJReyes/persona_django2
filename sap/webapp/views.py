from django.http import HttpResponse

from django.shortcuts import render
from personas.models import Personas

# Create your views here.
def bienvenido(request):
    no_personas = Personas.objects.count()
    #t_personas = Personas.objects.all()
    t_personas = Personas.objects.order_by('id')
    return render(request,'bienvenido.html', {'no_personas': no_personas, 't_personas': t_personas})
