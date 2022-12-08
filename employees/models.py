from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    fullname = models.CharField(max_length=30, null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.fullname)
