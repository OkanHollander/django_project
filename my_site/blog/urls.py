from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("all-posts", views.AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail"),
]
