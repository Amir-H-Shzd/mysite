from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(
        upload_to='blog/%Y/%m/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    # order items in general with Meta class not just showing in admin panel
    # and using class PostAdmin(admin.ModelAdmin):ordering = ['created_date'] in admin.py
    class Meta:
        ordering = ['-published_date']

    # change post name from id to title
    def __str__(self):
        return "{} - {}" .format(self.id, self.title)

    # a method to truncate content in blog-home template and you should be call {{post.snippets}} instead of {{post.content}} in blog-home
    # def snippets(self):
    #     return self.content[:100] + "..."
