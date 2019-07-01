from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from . import forms


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})


def article(request, pk):
  article = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post=article)

  if request.method == "POST":
    form = forms.CommentForm(request.POST)
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

def delete_comment(request, pk, comment_pk):
  comment = Comment.objects.get(id=comment_pk)
  post_id = pk
  if request.user.id == comment.author.id or \
     request.user.id == comment.post.author.id:
     comment.delete()
  return redirect('blog:article', pk=post_id)
