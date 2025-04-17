from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course


def home(request):
    return render(request, 'home.html')

def course_form(request):
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'course_form.html', {'form': form})

    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('./')

def course_list(request):
    context = {'courses' : Course.objects.all()}
    return render(request, 'course_list.html')

def course_enroll(request):
    return render(request, 'course_enroll.html')

def course_delete(request):
    return render(request, 'course_delete.html')