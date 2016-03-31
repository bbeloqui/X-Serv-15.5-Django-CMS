from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def mostrar(request, recurso):
    if request.method == "GET":     #request.method coge el metdodo que has mandado
        #fila = Pages.objects.get(name=recurso) #te coge el name de la tabla y
        try:
            fila = Pages.objects.get(name=recurso)
        except Pages.DoesNotExist:
			return HttpResponse("<b><h1>" + '<font color="red">' + 'Pagina no existente'
                                + '</font>' + "</h1></b>" )                                       #y pages por que es como se llama el class del model
        print fila.name
        return HttpResponse("<b><h1>Name: " + '<font color="blue">' + fila.name + '</font>'
                            + " , Id: " + '<font color="blue">' + str(fila.id) + '</font>'
                            + " , Page: " + '<font color="blue">' + fila.page + '</font>'
                            + "</h1></b>")


    #elif request.method == "PUT":
    #    otro = Pages(name=recurso, page=request.body)    #1    #2
    #    otro.save()   #guarda el name y page
    #    return HttpResponse("La pagina esta guardad")



#name:nombre
#Page: escribes lo que quieras
#con un put con http://localhost:8000/borja se crea(poster)
#y luego con poner en la url http://localhost:8000/borja se ve en el navegador
#el httpresponse que hemos puesto en el get
