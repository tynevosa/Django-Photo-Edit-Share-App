
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='picture')
    Description=models.TextField()
    Date= models.DateTimeField(auto_now_add=True)
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Visibility = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)

    def __str__(self):
        return self.Title

class Posts(models.Model):
    Comment=models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    By = models.ForeignKey(User, on_delete=models.CASCADE)
    Photoid = models.ForeignKey(Photo, on_delete=models.CASCADE)
    Replyid =models.IntegerField(default=0)
    Likes=models.IntegerField(default=0)

    def __str__(self):
        return self.Comment





