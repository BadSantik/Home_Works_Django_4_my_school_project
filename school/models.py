from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=10)
    teachers = models.ManyToManyField(Teacher, related_name='students')

    def __str__(self):
        return self.name
