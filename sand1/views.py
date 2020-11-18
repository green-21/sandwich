from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from .forms import WritePost
from .models import Post
from .view_account import login, is_login


# Create your views here.
def main_page(r):
    test =HttpRequest()
    
    user = is_login(r)
    if not user:
        return login(r)
    return render(r,"home.html")

def write_post(r):
    form = WritePost()
    return render(r, "write.html", { "form" : form })

def write_post_request(r):
    user = is_login(r)
    if not user:
        return login(r)
    if  r.method != "POST":
        return HttpResponse("잘못된 요청")
    
    pic = r.FILES['post_pic']
    data = Post(id = user)
    data.save()
    pic.name = data.pk
    data.picture = str(pic)
    data.save()
    return HttpResponseRedirect("")


# <page>
# login - register
# <authrity check>
# main - search - write - profile
# post - follow - setting

# <request>
# login -logout
# register

# like-unlike (post-comment)
# follow-unfollow
# write-delete (post - comment)
# profile setting
# 