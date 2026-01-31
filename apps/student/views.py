from django.shortcuts import render, redirect
from .models import Student

def Studentviews(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }

    return render(request, 'student.html', context)

def lan_switch_student(request, lan):
    return redirect(f'/{lan}/student/')