from django.contrib import admin
from .models import SavedProperty, RecentlyViewed

@admin.register(SavedProperty)
class SavedPropertyAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'saved_at')
    list_filter = ('saved_at',)

@admin.register(RecentlyViewed)
class RecentlyViewedAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'viewed_at')
    list_filter = ('viewed_at',)
