from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    taxid = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name