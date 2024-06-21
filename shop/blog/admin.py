from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
# Register your models here.

from .models import Post

def make_posts_published(modeladmin, request, queryset):
    resault = queryset.update(status = 'published')
    modeladmin.message_user(request, f'{resault} post(s) were successfully marked as published')

# make_posts_published.short_description = 'Make selected post(s) published'
make_posts_published.short_description = 'انتشار دادن پست ها'


def make_posts_draft(modeladmin, request, queryset):
    resault = queryset.update(status = 'draft')
    modeladmin.message_user(request, f'{resault} post(s) were successfully marked as draft')

# make_posts_draft.short_description = 'Make selected post(s) draft'
make_posts_draft.short_description = 'خارج کردن از حالت انتشار'

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type = "application/json")
    serializers.serialize("json", queryset, stream = response)
    return response

# export_as_json.short_description = 'Export selected posts as json'
export_as_json.short_description = 'برگرداندن به عنوان json'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('publish', 'status')
    search_fields = ('title', 'body')
    ordering = ['status','publish']
    actions = [make_posts_published, make_posts_draft, export_as_json,]



# admin.site.register(Post, PostAdmin)