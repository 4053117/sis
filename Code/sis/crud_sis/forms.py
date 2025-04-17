from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'is_published': 'Published?'
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)