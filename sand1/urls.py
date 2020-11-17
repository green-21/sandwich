from django.urls import path

from . import views
from . import view_account

urlpatterns = [
    path('login', view_account.login, name='login'),
    path('login_request', view_account.login_request, name='login_request'),
    path('register', view_account.register, name='register'),
    path('register_id_check',view_account.register_id_duplicate_check_ajax),
    path('register_request', view_account.register_request),
    # path('', views.index, name='index'),
]
