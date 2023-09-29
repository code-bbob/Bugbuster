from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=144)
    email= models.CharField(max_length=90)
    message= models.TextField()
    date=models.DateField()

    def __str__(self):
        return  self.name

class Post(models.Model):
    author = models.TextField(max_length=44)
    content = models.TextField() 
    date=models.DateField()

    def __str__(self):
        return self.author