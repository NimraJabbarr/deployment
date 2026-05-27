from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student, Teacher

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'students': students, 'teachers': teachers})
