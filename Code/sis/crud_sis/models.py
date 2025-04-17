from django.db import models

# Create your models here.

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name']
        permissions = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)
    content = models.TextField()
    instructors = models.ManyToManyField(Instructor)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title