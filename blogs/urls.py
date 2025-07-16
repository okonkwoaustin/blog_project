from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path("success", views.success, name="success"),
]
