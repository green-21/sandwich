from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import WritePost
from .models import Post, Account, Comment
from .view_account import login, is_login


# Create your views here.
def main_page(r):    
    user = is_login(r)
    if not user:
        return login(r)
    follows = user.follows.all()
    follows |= Account.objects.filter(id=user)
    posts = Post.objects.filter(id__in = follows).order_by("-created_on")[:15]
    return render(r,"home.html", { "posts" : posts, "user":user })

def search_page(r):
    user = is_login(r)
    if not user:
        return login(r)
    #시간 순으로
    accounts = Account.objects.all().order_by('created_on')
    return render(r, "search.html", { "accounts" : accounts, "user" : user })

def write_post(r):
    form = WritePost()
    return render(r, "write.html", { "form" : form })

def write_post_request(r):
    user = is_login(r)
    if not user:
        return login(r)
    if  r.method != "POST":
        return HttpResponse("잘못된 요청")

    data = Post(id = user, msg = r.POST['post_msg'], picture = r.FILES['post_pic'])
    data.save()
    return HttpResponseRedirect("/")

def profile_page(r, u_id):
    user = is_login(r)
    if not user:
        return login(r)
    host = get_object_or_404(Account,id=u_id)
    posts = Post.objects.filter(id =host).order_by('-created_on')
    return render(r,"profile.html", { "user" : user, "host" : host, "posts":posts })

def profile_setting(r):
    user = is_login(r)
    if not user:
        return login(r)
    print(user.picture)
    return render(r,"setting.html", {"user" : user})

def profile_setting_request(r):
    user = is_login(r)
    if not user:
        return login(r)
    if r.method != "POST":
        return HttpResponse("잘못된 요청")

    d = r.POST
    if d['formtype'] == 'set1':
        if d['pic_option'] == '0':
            user.picture = "/profile/default.png"
            user.save()
        elif d['pic_option'] == '1':
            user.picture = r.FILES['user_pic']
            user.save()
        else:
            return HttpResponse("잘못된 요청")
    elif d['formtype'] == 'set2':
        user.name = d['user_name']
        user.msg = d['user_msg']
        user.save()
    else:
        return HttpResponse("잘못된 요청")
    return HttpResponseRedirect('/u/'+user.id)

def post_page(r, p_id):
    user = is_login(r)
    if not user:
        return login(r)
    post = get_object_or_404(Post,no=p_id)
    return render(r,"post.html", { "post": post, "user":user })

def comment_request(r):
    user = is_login(r)
    if not user:
        return login(r)
    if r.method != "POST":
        return HttpResponseRedirect("/p/"+ r.POST['post-n'])
    
    try:
        post = Post.objects.get(no=r.POST['post-n'])
    except ObjectDoesNotExist:
        pass

    comment = Comment(id=user,msg=r.POST['comment-msg'], post_no=post)
    comment.save()

    return HttpResponseRedirect("/p/"+ r.POST['post-n'])

def like_request(r):
    user = is_login(r)
    if not user:
        return HttpResponse("-1")
    doc = r.GET['doc_type']
    try:
        if doc == "p":
            doc = Post.objects.get(no= r.GET['doc_no'])
        elif doc == 'c':
            doc = Comment.objects.get(no= r.GET['doc_no'])
        else:
            return HttpResponse("-1")
    except ObjectDoesNotExist:
        return HttpResponse("-1")

    if r.GET['action'] == 'l':
        if user in doc.likes.all():
            return HttpResponse("-1")
        doc.likes.add(user)
        return HttpResponse(doc.likes.count())
    elif r.GET['action'] == 'u':
        if not user in doc.likes.all():
            return HttpResponse("-1")
        doc.likes.remove(user)
        return HttpResponse(doc.likes.count())
    else:
        return HttpResponse("-1")

def follow_request(r):
    user = is_login(r)
    if not user:
        return HttpResponse("-1")

    if not Account.objects.filter(id = r.GET['to_id']).exists():
        return HttpResponse("-1")
    to_id = Account.objects.get(id = r.GET['to_id'])
    if to_id.id == user.id:
        return HttpResponse("-1")

    if r.GET['action'] == 'f':
        if Account.objects.filter(id=user, follows=to_id).exists():
            return HttpResponse("-1")
        user.follows.add(to_id)
        user.save()
    elif r.GET['action'] == 'u':
        if not Account.objects.filter(id=user, follows=to_id).exists():
            return HttpResponse("-1")
        user.follows.remove(to_id)
        user.save()
    else:
        return HttpResponse("-1")
    return HttpResponse("1")

# <page>
# login - register ㄲ
# <authrity check>
# main - search - write - profile ㄲ
# post - follow - setting ㄲ

# <request>
# login -logout ㄲ
# register ㄲ

# like-unlike (post-comment) ㄲ
# follow-unfollow ㄲ
# write-delete (post - comment) 
# profile setting
# 