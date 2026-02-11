from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Property
from inquiries.forms import InquiryForm
from dashboard.models import RecentlyViewed, SavedProperty
from django.contrib import messages

def property_list(request):
    properties = Property.objects.filter(status='available').order_by('-created_at')
    
    # Filtering
    location = request.GET.get('location')
    if location:
        properties = properties.filter(location__icontains=location)
        
    min_price = request.GET.get('min_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
        
    max_price = request.GET.get('max_price')
    if max_price:
        properties = properties.filter(price__lte=max_price)
        
    land_size = request.GET.get('land_size')
    if land_size:
        properties = properties.filter(land_size__gte=land_size)

    # Pagination
    paginator = Paginator(properties, 9) # 9 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'properties/property_list.html', context)

def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug)
    
    # Track Recently Viewed
    if request.user.is_authenticated:
        RecentlyViewed.objects.update_or_create(
            user=request.user, 
            property=property,
            defaults={'viewed_at': property.updated_at} # Just forcing update of viewed_at implicitly or explicitly
        )
        # Actually update_or_create updates timestamp if field is auto_now=True?
        # Standard auto_now=True updates on save() call. update_or_create calls save().
        # But let's be explicit if needed, or rely on auto_now.

    # Check if saved
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedProperty.objects.filter(user=request.user, property=property).exists()

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = property
            if request.user.is_authenticated:
                inquiry.user = request.user
            inquiry.save()
            # Send Email Logic Here (Optional/TODO)
            messages.success(request, 'Your inquiry has been submitted successfully!')
            return redirect('property_detail', slug=slug)
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.username, # Or full name
                'email': request.user.email,
                'phone': getattr(request.user, 'phone', '')
            }
        form = InquiryForm(initial=initial_data)

    return render(request, 'properties/property_detail.html', {
        'property': property,
        'form': form,
        'is_saved': is_saved
    })

@login_required
def toggle_save_property(request, slug):
    property = get_object_or_404(Property, slug=slug)
    saved_property, created = SavedProperty.objects.get_or_create(user=request.user, property=property)
    
    if not created:
        saved_property.delete()
        messages.info(request, 'Property removed from saved list.')
    else:
        messages.success(request, 'Property saved successfully.')
    
    return redirect('property_detail', slug=slug)
