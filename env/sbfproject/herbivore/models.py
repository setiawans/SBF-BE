from django.db import models

# Create your models here.
class Animal(models.Model) :
    name = models.CharField(max_length = 100)
    latin_name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)