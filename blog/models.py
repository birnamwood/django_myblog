from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  live = models.BooleanField(default=False)

  class Meta:  #メタクラス。順番をcreated_dateの降順にしている
      ordering = ['-created_date']

  def publish(self):
    self.published_date = timezone,now()
    self.save()

  def __str__(self):  #デフォルト
    return self.title


class Comment(models.Model):
  post = models.ForeignKey('Post', on_delete=models.CASCADE)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)


  class Meta:
    ordering = ['-created_date']
