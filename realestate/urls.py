from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('properties/', include('properties.urls')),
    path('inquiries/', include('inquiries.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('allauth.urls')), # Added Allauth URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
