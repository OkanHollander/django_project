from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm

# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering_fields = ["-date"]
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering_fields = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comments": CommentForm(),
            "tags": post.tag.all(),}
        return render(request, "blog/post-detail.html", context=context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        context = {
            "post": post,
            "comments": comment_form,
            "tags": post.tag.all(),}
        return render(request, "blog/post-detail.html", context=context)
