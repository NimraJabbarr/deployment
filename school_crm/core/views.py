from django.shortcuts import render   # Django ka render function import karte hain (HTML template ko load karne ke liye)
from .models import Student, Teacher  # Apne Student aur Teacher models ko import karte hain

# ✅ Home view function
def home(request):
    # Saare students ka data database se fetch karte hain
    students = Student.objects.all()
    
    # Saare teachers ka data database se fetch karte hain
    teachers = Teacher.objects.all()
    
    # 'home.html' template render karte hain aur usme students aur teachers ka data bhejte hain
    return render(request, 'home.html', {'students': students, 'teachers': teachers})
