from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'created_at')
    search_fields = ('title', 'location', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PropertyImageInline]
