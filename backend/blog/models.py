from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    author = models.TextField(max_length=44)
    title = models.CharField(max_length=255, default='')
    content = models.TextField()
 
    slug = models.SlugField(max_length=130)
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(**kwargs)
    
    date=models.DateField(default=now)
    def __str__(self):
        return 'Message from ' + self.title + ': ' + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
    