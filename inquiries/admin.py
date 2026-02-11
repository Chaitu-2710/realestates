from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'property', 'created_at', 'is_contacted')
    list_filter = ('is_contacted', 'created_at')
    search_fields = ('name', 'email', 'property__title')
    list_editable = ('is_contacted',)
