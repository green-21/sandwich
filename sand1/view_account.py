from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Account

def convert_account_to_token(account):
    return str(account.created_on) + "///" + account.id
    
def is_login(r):
    if r.session.get('token'):
        token = r.session.get('token').split("///")
        try:
            query_data = Account.objects.get(id=token[1], created_on=token[0])
            return query_data
        except ObjectDoesNotExist:
            return False
    else :
        return False


def login(r):
    if r.method == "POST":
        return login_request(r)
    return render(r,'login.html', { "msg" : "sand-hidden" })

def login_request(r):
    data = r.POST
    print("[정보]", str(data))
    try:
        query_data = Account.objects.get(id=data['user_id'], pw=data['user_pw'])
    except ObjectDoesNotExist:
        return render(r, 'login.html', {"msg": "."})
    print("로그인에 성공함")
    #success
    r.session['token'] = convert_account_to_token(query_data)
    return HttpResponseRedirect(r.path)



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
    print("[정보] 새로운 계정이 생성됨")
    return HttpResponseRedirect("/")
