from django.contrib import admin
from .models import Account, Post, Comment,Follow,PostLike,CommentLike

# Register your models here.
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(PostLike)
admin.site.register(CommentLike)

