from django.contrib import admin
from setting.models import *


class FAQAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'status'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'question',
        'answer',
    ]
    list_per_page = 10


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status'
    ]
    list_filter = [
        'created_date'
    ]
    search_fields = [
        'title'
    ]
    list_per_page = 10


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'tags',
        'publish'
    ]
    list_filter = [
        'created_date',
        'publish'
    ]
    search_fields = [
        'title',
        'tags',
        'publish'
    ]
    list_per_page = 10


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'tel',
        'website',
        'created_date',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'name',
        'email',
        'tel',
        'website',
        'text',
    ]
    list_per_page = 10


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'tel',
        'email',
        'status',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'full_name',
        'tel',
        'email',
    ]
    list_per_page = 10


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Slider)
admin.site.register(Notification)

