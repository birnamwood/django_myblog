from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})


def article(request, pk):
  article = Post.objects.get(id=pk)

  print(article)
  return render(request, 'blog/article.html',{ 'article': article })
