import uuid
from django.db import models
from django.utils.text import slugify

class Property(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
    )
    UNIT_CHOICES = (
        ('gunta', 'Gunta'),
        ('acre', 'Acre'),
        ('sqft', 'Sqft'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    land_size = models.DecimalField(max_digits=10, decimal_places=2)
    land_size_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    google_map_link = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slug = slugify(self.title)
            # Ensure slug is unique if necessary, but simple append is good for now
            self.slug = f"{unique_slug}-{str(uuid.uuid4())[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"
