from django.shortcuts import render

# Create your views here.
def course_form(request):
    return render(request, 'course_form.html')

def course_list(request):
    return render(request, 'course_list.html')

def course_enroll(request):
    return render(request, 'course_enroll.html')

def course_delete(request):
    return render(request, 'course_delete.html')