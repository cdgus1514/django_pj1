from django.shortcuts import render
from blog.models import Category, Post
from django.views import generic

# 작성하기
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# Create your views here.


def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }

    return render(req, 'index.html', context=context)


# 블로그 게시글 보여주는 클래스
class PostDetailView(generic.DetailView):
    model = Post


# 블로그에서 글쓰기 클래스
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'title_image', 'content', 'category']
