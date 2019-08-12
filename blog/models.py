from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)

    date_of_creation = models.DateField(auto_now_add=True)

    text = models.TextField(max_length=2000, help_text='Your blog post')

    class Meta:
        ordering = ['-date_of_creation']

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=500, help_text='Information about this author.')

    class Meta:
        ordering = ['user', 'bio']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.user.username}'

class BlogComment(models.Model):
    description = models.TextField(max_length=200, help_text='Your comment for the blog post.')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    post_date = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        len_title = 75
        if len(self.description)> len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring



