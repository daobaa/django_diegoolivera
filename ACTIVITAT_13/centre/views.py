from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index_one(request):
    return HttpResponse("Hello, world")
def index(request):
    professor = {"name": "Sergi", "surname1": "Franco", "mail":"sfranco@iticbcn.cat"}
    template = loader.get_template('index.html')
    data = template.render({"nom":professor["name"], "cognom1":professor["surname1"], "correu":professor["mail"]})
    return HttpResponse(data)
def students(request):
    template = loader.get_template('students.html')
    return HttpResponse(template.render())
def teachers(request):
    template = loader.get_template('teachers.html')
    return HttpResponse(template.render())