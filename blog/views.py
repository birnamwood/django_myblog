from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .import forms


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})


def article(request, pk):
  article = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post=article)

  if request.method == "POST":
    form = forms.commentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = article
      comment.author = request.user
      comment.save()
  else:
    form = forms.CommentForm()

  print(article)
  return render(request, 'blog/article.html',{
     'article': article,
     'form': form,
     'comments': comments
     })
