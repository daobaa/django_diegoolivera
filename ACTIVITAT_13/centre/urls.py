from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one, name='index_one'),
    path('index', views.index, name='index'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name='teachers')
]