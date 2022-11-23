from ast import If
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template,Context
from EasyPark_Pyton.models import Persona
from django.db import connection
from django.shortcuts import render,redirect
from django.contrib import messages

def inicio(request):
    return render(request,'index.html')

def buscar(request):
    return render(request,'buscar.html')

def login(request):
    return render(request,'login.html')

def publicar(request):
    return render(request,'publicar.html')

#region persona 
def registropersona(request):
    if request.method=="POST":
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('cedula') and request.POST.get('email') and request.POST.get('tel_usuario') and request.POST.get('nombre_usuario') and request.POST.get('contraseña') and request.POST.get('id_rol'):
            persona= Persona()
            persona.nombres= request.POST.get('nombres') 
            persona.apellidos= request.POST.get('apellidos')
            persona.cedula= request.POST.get('cedula')  
            persona.email= request.POST.get('email') 
            persona.tel_usuario= request.POST.get('tel_usuario') 
            persona.nombre_usuario= request.POST.get('nombre_usuario') 
            persona.contraseña= request.POST.get('contraseña') 
            persona.id_rol= request.POST.get('id_rol') 
            insertar=connection.cursor()
            insertar.execute("call insertarusuario('"+persona.nombres+"','"+persona.apellidos+"','"+persona.cedula+"','"+persona.email+"','"+persona.tel_usuario+"','"+persona.nombre_usuario+"','"+persona.contraseña+"','"+persona.id_rol+"')")
            messages.success(request, "El usuario: " +persona.nombres+persona.apellidos+ " se guardó con exito")
            return render(request,'registro.html')
    else:
        return render(request,'registro.html')

#Aqui esta redireccionado a usuario ya que me imagino que va aser el listado de usuarios registrados con su rol
def Borrarcliente(request,id):
    persona=Persona.objects.get(id=id)
    persona.delete()
    return redirect("/Usuarios/listado/")

def Actualizarcliente(request,id):
    if request.method=="POST":
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('cedula') and request.POST.get('email') and request.POST.get('tel_usuario') and request.POST.get('nombre_usuario') and request.POST.get('contraseña') and request.POST.get('id_rol'):
            persona= Persona()
            persona.nombres= request.POST.get('nombres') 
            persona.apellidos= request.POST.get('apellidos')
            persona.cedula= request.POST.get('cedula')  
            persona.email= request.POST.get('email') 
            persona.tel_usuario= request.POST.get('tel_usuario') 
            persona.nombre_usuario= request.POST.get('nombre_usuario') 
            persona.contraseña= request.POST.get('contraseña') 
            persona.id_rol= request.POST.get('id_rol')
            actualizar=connection.cursor()
            id=str(id)
            actualizar.execute("call actualizausuario('"+persona.nombres+"','"+persona.apellidos+"','"+persona.cedula+"','"+persona.email+"','"+persona.tel_usuario+"','"+persona.nombre_usuario+"','"+persona.contraseña+"','"+persona.id_rol+"')")
            return redirect('/Usuarios/listado/')
    else:
        unsolousuario=Persona.objects.filter(id=id)
        return render(request,'Usuarios/actualizar.html',{'unsolousuario':unsolousuario})
    

