from django.db import models

# Create your models here.

class login(models.Model):
    uName = models.CharField(max_length= 30)
    uPassword = models.CharField(max_length= 30)

    def __str__(self):
        return self.uName

class birthday(models.Model):
    eName = models.CharField(max_length= 80)
    eDesignation = models.CharField(max_length= 50)
    workLocation = models.CharField(max_length= 50)
    DOB = models.CharField(max_length= 20)
    DOJ = models.CharField(max_length= 20)
    eContact = models.CharField(max_length= 15)

    def __str__(self):
        return self.eName
