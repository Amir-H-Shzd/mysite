from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    # order items in general with Meta class not just showing in admin panel
    # and using class PostAdmin(admin.ModelAdmin):ordering = ['created_date'] in admin.py
    class Meta:
        ordering = ['-created_date']

    # change post name from id to title
    def __str__(self):
        return "{} - {}" .format(self.id, self.name)
