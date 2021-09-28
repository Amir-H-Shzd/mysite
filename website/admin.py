from django.contrib import admin
from website.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email',
                    'created_date')
    list_filter = ('subject', 'email')
    # ordering = ['created_date']
    search_fields = ['name', 'message']
