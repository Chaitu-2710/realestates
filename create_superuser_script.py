
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
password = "adminpassword123"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser created successfully.")
    print(f"Username: {username}")
    print(f"Password: {password}")
else:
    print(f"Superuser '{username}' already exists.")
    # Optional: Reset password if needed, but let's stick to simple creaation for now.
