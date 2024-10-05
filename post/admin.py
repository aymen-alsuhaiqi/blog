from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date')
    list_filter = ('author', 'created_date')
    search_fields = ('title', 'author__username')
admin.site.register(Post, PostAdmin)

admin.site.register(Comment)