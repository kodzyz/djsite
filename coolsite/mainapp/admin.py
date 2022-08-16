from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'user', 'create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'text')
    list_filter = ('create',)

admin.site.register(Article, ArticleAdmin)