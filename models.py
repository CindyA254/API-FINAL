from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
