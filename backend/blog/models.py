from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.TextField(max_length=44)
    content = models.TextField() 
    date=models.DateField()

    def __str__(self):
        return self.author