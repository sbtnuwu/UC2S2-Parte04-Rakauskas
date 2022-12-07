from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.

def menu(request):
    mensaje="""
        <h1>Proyecto de Desarrollo Web LP III</h1>
        <h2>Opciones:</h2>
        <ul>
            <li><a href="http://127.0.0.1:8000/inicio/">Inicio</a>
        </ul>
    """
    return HttpResponse(mensaje)

def inicio(request):
    mensaje="""
        <h1>Lenguaje de Programación III</h1>
        <h2>Integrantes del Grupo:</h2>
        <ul>
            <li>Miguel Angel Prado Zuta
            <li>Sebastian Alberto Rakauskas Purca
            <li>Diego Alejandro Quispe Cancho
        </ul>
    """
    return HttpResponse(mensaje)
