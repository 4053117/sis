from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)
    inst_id = models.ManyToManyField(Instructor)
    content = models.TextField()