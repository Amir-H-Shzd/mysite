from django.contrib import admin
from blog.models import Post
# Register your models here.

# admin.site.register(Post)  || another method for register post to admin panel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'created_date',
                    'published_date', 'views', 'status')
    list_filter = ('status',)
    # ordering = ['created_date']
    search_fields = ['title', 'content']
