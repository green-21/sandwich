from django.http import HttpRequest, HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Account

def is_login():
    pass
def login(r):
    return render(r,'login.html')
def login_request(r):
    if r.method != "POST":
        return HttpResponse("잘못된 요청")
    data = r.POST
    # data."name" 으로 접근
    return HttpResponse("성공^^")
    
def register(r):
    return render(r,'register.html')
def register_id_duplicate_check_ajax(r):
    user_id = r.GET.get('user_id')
    try:
        Account.objects.get(id=user_id)
        return HttpResponse("0")
    except ObjectDoesNotExist:
        return HttpResponse("1")
    
def register_request(r):
    if r.method != "POST":
        return HttpResponse("잘못된 요청")
    d = r.POST
    new_account = Account(id=d["user_id"],pw=d["user_pw"],name=d["user_name"])
    new_account.save()
    return HttpResponseRedirect("login")
