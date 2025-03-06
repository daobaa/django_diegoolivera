from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def students(request):
    student = {"name":"Diego Andres", "surname1":"Olivera", "surname2":"Abarca", "mail":"2024_diego.olivera@iticbcn.cat", "course":"DAW2", "modules":"Tots"}
    return render(request, 'students.html', {"nom":student["name"], "cognom1":student["surname1"], "cognom2":student["surname2"], "correu":student["mail"], "curs":student["course"], "moduls":student["modules"]})

def student(request):

def teachers(request):
    professor = {"name":"Sergi", "surname1":"Franco", "surname2":"Gonzalez", "mail":"sfranco@iticbcn.cat", "course":"DAW2", "thutor":"Header", "modules":"M14"}
    return render(request, 'teachers.html', {"nom":professor["name"], "cognom1":professor["surname1"], "cognom2":professor["surname2"], "correu":professor["mail"], "curs":professor["course"], "tutor":professor["thutor"], "moduls_imp":professor["modules"]})

def teacher(request):
