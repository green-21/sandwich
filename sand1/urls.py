from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import view_account, views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('register', view_account.register, name='register'),
    path('register_id_check',view_account.register_id_duplicate_check_ajax),
    path('register_request', view_account.register_request),
    path('write', views.write_post, name="write_post"),
    path("write_request", views.write_post_request)
    # path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
