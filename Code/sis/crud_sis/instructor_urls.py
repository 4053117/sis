from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list),
    path('form/', views.course_form),
    path('enroll/', views.course_enroll),
    path('delete/', views.course_delete),
]
