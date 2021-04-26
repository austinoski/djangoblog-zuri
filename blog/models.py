from django.db import models

from django.urls import reverse_lazy


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('post-detail', args=[str(self.id)])


class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __repr__(self):
        return "comment {}".format(self.id)
    
    def __str__(self):
        return "comment {}".format(self.id)
