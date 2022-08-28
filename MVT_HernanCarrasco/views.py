from django.http import HttpResponse
from django.template import loader, context, Template

def prueba_template1(request):

    nom="kdfcnsfc"
    ape="sdjddisfn"
    lista=[1,2,3,4,5,6,7,8,9,0]
    dict={'nombre':nom, 'apellido':ape, 'lista':lista}

    plantilla=loader.get_template('plantilla1.html')

    documento=plantilla.render(dict)
    return HttpResponse(documento)
