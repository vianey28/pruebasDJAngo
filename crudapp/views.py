from django.shortcuts import render
from .models import Publisher
from .forms import FormularioPublisher
from django.http import HttpResponseRedirect

def mostrarTabla(request):
    datos = Publisher.objects.all()
    return render(request, 'crudapp/search.html', {'datos':datos})

def formulario(request):
   
	formulario = FormularioPublisher()
	return render(request, 'crudapp/agregarPublisher.html', {'formulario': formulario})

    #if request.method=="POST":
        #formulario=FormularioPublisher(request.POST)
        #if formulario.is_valid():
            #formulario.save()
            #return HttpResponseRedirect("/tabla")
    #else:
        #formulario=FormularioPublisher()
    #return render(request, 'crudapp/agregarPublisher.html', {'formulario': formulario})