from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("upload/", views.upload, name="upload"),
    path("comments/<int:id>", views.post_comment, name="comment"),
    path("search/", views.search_results, name="search_results"),
    path("accounts/register/", views.register, name="register"),
    path("like/<int:id>/", views.like_image, name="like_image"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
