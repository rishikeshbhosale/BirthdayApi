from django.db import models

# Create your models here.

class login(models.Model):
    uName = models.CharField(max_length=30)
    uPassword = models.CharField(max_length=30)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class worklocation(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location

class designation(models.Model):
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.designation


class birthday(models.Model):
    eName = models.CharField(max_length=80)
    eDesignation = models.ForeignKey(designation, default=1, on_delete=models.SET_DEFAULT)
    workLocation = models.ForeignKey(worklocation, default=1, on_delete=models.SET_DEFAULT)
    DOB = models.CharField(max_length=20)
    DOJ = models.CharField(max_length=20)
    eContact = models.CharField(max_length=15)

    def __str__(self):
        return self.eName
