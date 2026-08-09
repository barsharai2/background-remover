from django.db import models

# Create your models here.
class Student(models.Model):
    
    image=models.FileField( upload_to='images',null=True)

   