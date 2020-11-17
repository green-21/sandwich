from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import LoginForm
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
    print(data)

    return HttpResponse("성공^^")
def register(r):
    return render(r,'register.html')
def register_id_duplicate_check_ajax():
    pass
def register_request(r):
    if r.method != "POST":
        return HttpResponse("잘못된 요청")
    data = r.POST
    print(data)
    return HttpResponse("성공 ^^")
