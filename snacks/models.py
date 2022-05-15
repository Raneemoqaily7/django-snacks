
from django.db import models

class Snack (models.Model):
    name = models.CharField(max_length=255)
    description =models.TextField()
    
    


    def __str__(self) :
        return self.name 

class HealthySnack (models.Model):
    name = models.CharField(max_length=255)
    description =models.TextField()
    price =models.IntegerField()
    is_healthy=models.BooleanField()
    
    


    def __str__(self) :
        return self.name 
