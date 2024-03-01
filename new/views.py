from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . models import Teacher


# Create your views here.

def index(request):
    return render(request, 'index.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def students(request):
    student = Student.objects.all()
    return render(request, 'students .html',{"students": student})

def teachers(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html', {"teachers": teacher})

def insert(request):
    return render(request, 'insert.html')



