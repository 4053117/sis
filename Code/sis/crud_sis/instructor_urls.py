from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:id>/', views.course_form, name= 'course_view'),
    path('<int:id>/enroll/', views.course_enroll, name='course_enroll'),
    path('<int:id>/delete/', views.course_delete, name='course_delete'),
]
