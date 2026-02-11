
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.settings")
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_dummy_google_app():
    # Get the current site (default is ID=1, example.com)
    try:
        site = Site.objects.get(id=1)
        site.domain = '127.0.0.1:8000'
        site.name = 'Real Estate Local'
        site.save()
        print(f"Updated Site ID 1 to {site.domain}")
    except Site.DoesNotExist:
        site = Site.objects.create(domain='127.0.0.1:8000', name='Real Estate Local')
        print("Created new Site configuration")

    # Check if Google App exists
    provider_id = 'google'
    try:
        app = SocialApp.objects.get(provider=provider_id)
        print(f"SocialApp '{provider_id}' already exists.")
    except SocialApp.DoesNotExist:
        print(f"Creating placeholder SocialApp for {provider_id}...")
        app = SocialApp.objects.create(
            provider=provider_id,
            name='Google Auth (Placeholder)',
            client_id='YOUR_CLIENT_ID_HERE',
            secret='YOUR_SECRET_KEY_HERE',
        )
        app.sites.add(site)
        print(f"Created placeholder SocialApp. PLEASE UPDATE CREDENTIALS IN ADMIN PANEL.")

if __name__ == "__main__":
    setup_dummy_google_app()
