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
            <li><a href="http://127.0.0.1:8000/examen/">Examen</a>
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

def examen(request):
    mensaje="""
        <h1>Lenguaje de Programación III</h1>
        <h2>GitHub del Proyecto</h2>
        <ul>
            <li>Nombre del Estudiante 01: Sebastian Alberto Rakauskas Purca <br>
                GitHub: <a href="https://github.com/sbtnuwu/UC3S2_Parte01_Rakauskas">https://github.com/sbtnuwu/UC3S2_Parte01_Rakauskas.git</a>  
            </li>
            <br>
            <li>Nombre del Estudiante 02: Miguel Angel Prado Zuta <br>
                    GitHub: <a href="https://github.com/mikprz/UC2S2-Parte02-Prado-Zuta">https://github.com/mikprz/UC2S2-Parte02-Prado-Zuta.git</a>
            </li>
            <br>
            <li>Nombre del Estudiante 03: Diego Alejandro Quispe Cancho <br>
                    GitHub: <a href="https://github.com/DieGodV3/UC2S2-Parte03-Quispe">https://github.com/DieGodV3/UC2S2-Parte03-Quispe.git</a>
            </li>
            <br>
            <li>Nombre del Estudiante 04: Sebastian Alberto Rakauskas Purca <br>
                    GitHub: <a href="https://github.com/sbtnuwu/UC2S2-Parte04-Rakauskas">https://github.com/sbtnuwu/UC2S2-Parte04-Rakauskas.git</a>
            </li>
        </ul>
    """
    return HttpResponse(mensaje)