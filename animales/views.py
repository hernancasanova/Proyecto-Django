from django.shortcuts import render_to_response
from django.http import HttpResponse
from animales.models import Animales

# Create your views here.
def imagen18132(request):
    number=Animales.objects.get(nombre="clavela")
    return render_to_response('18132.html',{'hernan':number})
    #return render(request,'18132.html')
    #return HttpResponse("Hola mundo")
