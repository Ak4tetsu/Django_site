from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'poblish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('poblish', 'status')
    search_fields = ('title', 'body')
    ordering = ['status','poblish']



# admin.site.register(Post, PostAdmin)