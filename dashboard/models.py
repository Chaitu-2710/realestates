from django.db import models
from django.conf import settings
from properties.models import Property

class SavedProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Saved Properties"
        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user} saved {self.property}"

class RecentlyViewed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recently_viewed')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Recently Viewed"
        ordering = ['-viewed_at']
        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user} viewed {self.property}"
