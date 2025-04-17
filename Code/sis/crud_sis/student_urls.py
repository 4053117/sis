from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:id>/enroll/', views.course_enroll, name='course_enroll'),
]
