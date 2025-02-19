from django.contrib import admin
from pages.models import ContactModel
from . import models

@admin.register(ContactModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'created_at']
    search_fields = ['message', 'full_name']
    list_filter = ['created_at', 'email']

@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'job',)
    search_fields = ('name', 'job',)
    list_filter = ('job',)