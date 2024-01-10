from django.shortcuts import render
from datetime import date
from .models import Post

def get_date(post):
    return post["date"]

# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "latest_posts": latest_posts
    })

def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": dummy_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in dummy_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
