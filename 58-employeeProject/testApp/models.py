from django.db import models


class Employee(models.Model):
    eno = models.SmallIntegerField()
    ename = models.CharField(max_length=20)
    esal = models.FloatField()
    eaddr = models.TextField()

    def __str__(self):
        return self.ename

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        ordering = ('-ename',)

