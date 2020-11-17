from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=20, primary_key="true")
    pw = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    msg = models.CharField(max_length=200, blank="true", default="")
    time = models.DateTimeField('date published')

class Post(models.Model):
    no = models.AutoField(primary_key="true")
    id = models.ForeignKey(Account, on_delete=models.CASCADE)
    picture = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)
    time = models.DateTimeField('date published')

class Comment(models.Model):
    no = models.AutoField(primary_key="true")
    post_no = models.ForeignKey(Post, on_delete=models.CASCADE)
    id = models.ForeignKey(Account,on_delete=models.CASCADE)
    msg = models.CharField(max_length=200)
    time = models.DateTimeField('date published')

class Follow(models.Model):
    no = models.AutoField(primary_key="true")
    from_id = models.ManyToManyField(Account, related_name="from_user")
    to_id = models.ManyToManyField(Account, related_name="to_user")

class PostLike(models.Model):
    no = models.AutoField(primary_key="true")
    post_no = models.ForeignKey(Post, on_delete=models.CASCADE)
    id = models.ForeignKey(Account, on_delete=models.CASCADE)

class CommentLike(models.Model):
    no = models.AutoField(primary_key="true")
    comment_no = models.ForeignKey(Comment, on_delete=models.CASCADE) 
