from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inquiries.models import Inquiry
from .models import SavedProperty, RecentlyViewed

@login_required
def dashboard(request):
    inquiries = Inquiry.objects.filter(user=request.user).order_by('-created_at')
    saved_properties = SavedProperty.objects.filter(user=request.user).order_by('-saved_at')
    recently_viewed = RecentlyViewed.objects.filter(user=request.user).order_by('-viewed_at')[:10]
    
    return render(request, 'dashboard/dashboard.html', {
        'inquiries': inquiries,
        'saved_properties': saved_properties,
        'recently_viewed': recently_viewed
    })
