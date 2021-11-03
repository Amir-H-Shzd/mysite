from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

# admin.site.register(Post)  || another method for register post to admin panel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'created_date',
                    'published_date', 'views', 'status', 'id')
    list_filter = ('status', 'author')
    # ordering = ['created_date']
    search_fields = ['title', 'content']

# this is a method like in above foe registering new table Category

# @admin.register(Category)
# class CaregoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category)
