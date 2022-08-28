from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

lista=[]

def mostrar_fam(request):
    return HttpResponse(lista)

def crear_fam(request):
    pariente1=Familiar(nombre="Lesbia", fecha_nacimiento="1952-5-31", edad=69, parentesco="Mama")
    pariente2=Familiar(nombre="Hernan V.", fecha_nacimiento="1947-8-13", edad=75, parentesco="Papa")
    pariente3=Familiar(nombre="Marian", fecha_nacimiento="1952-8-26", edad=29, parentesco="Hermana")
    pariente1.save()
    pariente2.save()
    pariente3.save()
    lista.append(pariente1)
    lista.append(pariente2)
    lista.append(pariente3)
    msg=f"Familiar creado: Nombre: {pariente1.nombre} Fecha de Nacimiento: {pariente1.fecha_nacimiento} Edad: {pariente1.edad} Parentesco: {pariente1.parentesco}\n Familiar creado: Nombre: {pariente2.nombre} Fecha de Nacimiento: {pariente2.fecha_nacimiento} Edad: {pariente2.edad} Parentesco: {pariente2.parentesco}\n Familiar creado: Nombre: {pariente3.nombre} Fecha de Nacimiento: {pariente3.fecha_nacimiento} Edad: {pariente3.edad} Parentesco: {pariente3.parentesco}"
    return HttpResponse(msg)
