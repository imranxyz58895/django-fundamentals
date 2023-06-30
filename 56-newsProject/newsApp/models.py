from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    marks = models.SmallIntegerField()

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    

