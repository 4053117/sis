from django.shortcuts import render
from .forms import CourseForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def course_form(request):
    form = CourseForm()

    return render(request, 'course_form.html', {'form': form})

def course_list(request):
    return render(request, 'course_list.html')

def course_enroll(request):
    return render(request, 'course_enroll.html')

def course_delete(request):
    return render(request, 'course_delete.html')