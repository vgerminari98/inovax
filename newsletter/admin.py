from django.contrib import admin
from .models import NewsletterSubscriber

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'is_active')
    search_fields = ('nome', 'email')
    list_filter = ('is_active',)
