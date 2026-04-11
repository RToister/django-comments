from django.urls import path
from . import views

urlpatterns = [
    path("", views.comment_list),
    path("comments/", views.comment_list),
    path("comments/create/", views.comment_create),
    path("comments/preview/", views.comment_preview),
    path("comments/<int:pk>/reply/", views.comment_reply),
    path("file/<int:pk>/", views.file_view, name="file_view"),
]
