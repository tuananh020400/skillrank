from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    taxid = models.CharField(max_length=255, unique=True)
    major = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name