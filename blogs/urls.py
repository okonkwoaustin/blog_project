from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path("success", views.success, name="success"),
    path("blogs/<int:blog_id>/", views.blog_detail, name="blog-detail"),
    path("blogs/<int:blog_id>/edit", views.blog_update, name="blog-update"),
    path("blogs/<int:blog_id>/delete", views.blog_delete, name="blog-delete"),
]
