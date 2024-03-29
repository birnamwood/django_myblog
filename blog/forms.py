from django import forms
from . import models


class CommentForm(forms.ModelForm):
  class Meta:
    model = models.Comment
    fields = ('name', 'text',)
    

class PostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    fields = ('title', 'text',)
    #exclude = ('title',)と書いて除外指定のみ行うこともできる


class SearchForm(forms.Form):
  q = forms.CharField(label="検索")

