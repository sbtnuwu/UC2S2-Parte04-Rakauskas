from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
import os
from flask import Flask,redirect

# Create your views here.

def menu(request):
    mensaje="""
        <h1>Proyecto de Desarrollo Web LP III</h1>
        <h2>Opciones:</h2>
        <ul>
            <li><a href="http://127.0.0.1:8000/inicio/">Inicio</a>
            <li><a href="http://127.0.0.1:8000/rango/">Nuemros primos de a a b </a>
            <li><a href="http://127.0.0.1:8000/rango2/">Numeros primos de a a b a < b </a>
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


def rango(request):
    a = 1
    b = 20
    bandera = 0

    resultado = f"""
        <h2>Números primos de [{a}, {b}]</h2>
        Resultado: <br>
        <ul>
    """

    for i in range(a,b):
        if i == 1:
            bandera = 1
        for x in range(2,i-1):
            if i%x == 0:
                bandera = 1
                
        if bandera == 0:
            resultado += f"""
                        <li>{i}</li>
                    """
        bandera = 0   

    return HttpResponse(resultado)

def rango2(request, a =1, b = 20):
    if a > b:
        return redirect("http://127.0.0.1:8000/rango2/", a = b, b = a)

    a = 1
    b = 20
    bandera = 0

    resultado = f"""
        <h2>Números primos de [{b}, {a}]</h2>
        Resultado: <br>
        <ul>
    """

    for i in range(a,b):
        if i == 1:
            bandera = 1
        for x in range(2,i-1):
            if i%x == 0:
                bandera = 1
                
        if bandera == 0:
            resultado += f"""
                        <li>{i}</li>
                    """
        bandera = 0   

    return HttpResponse(resultado)
