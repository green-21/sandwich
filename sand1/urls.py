from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import view_account, views


urlpatterns = [
    path('', views.main_page, name='main_page'),

    path('register', view_account.register, name='register'),
    path('register_id_check',view_account.register_id_duplicate_check_ajax),
    path('register_request', view_account.register_request),

    path('search', views.search_page, name='search'),
    path('write', views.write_post, name="write_post"),
    path("write_request", views.write_post_request),
    path('u/<str:u_id>', views.profile_page, name='profile'),
    path('profile_setting_request', views.profile_setting_request),

    path('p/<int:p_id>', views.post_page, name='post'),
    path('comment_request', views.comment_request),
    path('like_request', views.like_request),
    path('follow_request', views.follow_request),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
