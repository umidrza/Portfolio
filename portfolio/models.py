from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    education = models.CharField(max_length=50)
    experiences = models.TextField()
    skills = models.TextField()
    hobbies = models.TextField()
    languages = models.CharField(max_length=50)
    social_accounts = models.TextField()

    def __str__(self):
        return self.name
    

    