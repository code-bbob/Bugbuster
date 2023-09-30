from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.TextField(max_length=44)
    title = models.CharField(max_length=255, default='')
    content = models.TextField()
    slug = models.CharField(max_length=130, null=True, blank=True) 
    date=models.DateField()

    def __str__(self):
        return 'Message from ' + self.title + ': ' + self.author