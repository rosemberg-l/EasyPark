from ast import If
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template,Context
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

def registro(request):
    return render(request,'registro.html')

