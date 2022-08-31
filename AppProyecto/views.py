from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar, Curso
from django.template import loader

lista=[]

def mostrar_fam(request):
    dict_cont={'lista':lista}
    plantilla=loader.get_template('plantilla2.html')
    documento=plantilla.render(dict_cont)
    return HttpResponse(documento)


def crear_fam1(request):
    pariente1=Familiar(nombre="Lesbia", fecha_nacimiento="1952-5-31", edad=69, parentesco="Madre")
    pariente1.save()
    lista.append(pariente1)
    msg=f"Familiar creado: Nombre: {pariente1.nombre} Fecha de Nacimiento: {pariente1.fecha_nacimiento} Edad: {pariente1.edad} Parentesco: {pariente1.parentesco}"
    return HttpResponse(msg)

def crear_fam2(request):
    pariente2=Familiar(nombre="Hernan V.", fecha_nacimiento="1947-8-13", edad=75, parentesco="Padre")
    pariente2.save()
    lista.append(pariente2)
    msg=f"Familiar creado: Nombre: {pariente2.nombre} Fecha de Nacimiento: {pariente2.fecha_nacimiento} Edad: {pariente2.edad} Parentesco: {pariente2.parentesco}"
    return HttpResponse(msg)

def crear_fam3(request):
    pariente3=Familiar(nombre="Marian", fecha_nacimiento="1952-8-26", edad=29, parentesco="Hermana")
    pariente3.save()
    lista.append(pariente3)
    msg=f"Familiar creado: Nombre: {pariente3.nombre} Fecha de Nacimiento: {pariente3.fecha_nacimiento} Edad: {pariente3.edad} Parentesco: {pariente3.parentesco}"
    return HttpResponse(msg)



def curso(request):

    
    nombre = request.POST.get("nombre")
    comision = request.POST.get("comision")
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    curso=Curso(nombre="curso creado en el ejemplo", comision=0)
    print("CREANDO CURSO")
    curso.save()
    
    texto=f"curso creado"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "AppProyecto/inicio.html")

def cursos(request):
    return render (request, "AppProyecto/cursos.html")


def estudiantes(request):
    return render (request, "AppProyecto/estudiantes.html")

def profesores(request):
    return render (request, "AppProyecto/profesores.html")

def entregables(request):
    return render (request, "AppProyecto/entregables.html")
