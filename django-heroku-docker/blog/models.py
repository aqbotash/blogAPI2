from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    