from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.TextField(max_length=44)
    title = models.CharField(max_length=255, default='')
    content = models.TextField() 
    date=models.DateField()

    def __str__(self):
        return self.author