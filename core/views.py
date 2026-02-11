from django.shortcuts import render
from properties.models import Property

def home(request):
    featured_properties = Property.objects.filter(is_featured=True, status='available')[:6]
    latest_properties = Property.objects.filter(status='available').order_by('-created_at')[:6]
    return render(request, 'core/home.html', {
        'featured_properties': featured_properties,
        'latest_properties': latest_properties
    })

def contact(request):
    return render(request, 'core/contact.html')
