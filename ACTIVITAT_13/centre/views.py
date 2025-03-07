from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

students_list = [
    {
        "id": "1",
        "nom": "Diego Andrés",
        "cognom1": "Olivera",
        "cognom2": "Abarca",
        "correu": "2024_diego.olivera@iticbcn.cat",
        "curs": "2n DAW",
        "moduls": "Tots"
    },
    {
        "id": "2",
        "nom": "Alena",
        "cognom1": "Morozova",
        "cognom2": "Revaka",
        "correu": "2024_alena.morozova@iticbcn.cat",
        "curs": "2n DAM",
        "moduls": "Tots"
    },
    {
        "id": "3",
        "nom": "Luis Ángel",
        "cognom1": "Montiel",
        "cognom2": "Ceballo",
        "correu": "2024_luis.montiel@iticbcn.cat",
        "curs": "2n DAW",
        "moduls": "Tots"
    }
]
teachers_list = [
    {
        "id": "1",
        "nom": "Sergi",
        "cognom1": "Franco",
        "cognom2": "González",
        "correu": "sergi.franco@iticbcn.cat",
        "curs": "2n DAW",
        "tutor": "Cap",
        "moduls_imp": "M14"
    },
    {
        "id": "2",
        "nom": "Antonio",
        "cognom1": "Limón",
        "cognom2": "Morón",
        "correu": "antonio.limon@iticbcn.cat",
        "curs": "1r DAW",
        "tutor": "Cap",
        "moduls_imp": "M1"
    },
    {
        "id": "3",
        "nom": "Montse",
        "cognom1": "Calopa",
        "cognom2": "Mars",
        "correu": "montse.calopa@iticbcn.cat",
        "curs": "2n ASIX",
        "tutor": "Cap",
        "moduls_imp": "M7"
    }
]

def index(request):
    return HttpResponse('Hello, world')

def students(request):
    student_Obj = students_list
    return render(request, 'students.html', {'students': student_Obj})

def student(request, pk):
    student_Obj = None
    for i in students_list:
        if i['id'] == pk:
            student_Obj = i
    return render(request, 'student.html', {'student': student_Obj})

def teachers(request):
    teacher_Obj = teachers_list
    return render(request, 'teachers.html', {'teachers': teacher_Obj})

def teacher(request, pk):
    teacher_Obj = None
    for i in teachers_list:
        if i['id'] == pk:
            teacher_Obj = i
    return render(request, 'teacher.html', {'teacher': teacher_Obj})