from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=20, primary_key="true")
    pw = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, upload_to="profile", default='/profile/default.png')
    name = models.CharField(max_length=20)
    msg = models.CharField(max_length=200, blank="true", default="")
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    follows = models.ManyToManyField('self', related_name="followers", symmetrical=False, blank=True)
    def __str__(self):
        return self.id

class Post(models.Model):
    no = models.AutoField(primary_key="true")
    id = models.ForeignKey(Account, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, upload_to="post")
    msg = models.CharField(max_length=200)
    likes = models.ManyToManyField(Account, related_name="like_posts", blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    

class Comment(models.Model):
    no = models.AutoField(primary_key="true")
    post_no = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    id = models.ForeignKey(Account,on_delete=models.CASCADE)
    msg = models.CharField(max_length=200)
    likes = models.ManyToManyField(Account, related_name="like_comments", blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    