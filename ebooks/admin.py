from django.contrib import admin
from .models import Ebook

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title','is_active')
    fields = ('title', 'file', 'cover_image', 'uploaded_at')
    readonly_fields = ('uploaded_at',)