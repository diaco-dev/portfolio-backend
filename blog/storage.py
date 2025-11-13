import os
from urllib.parse import urljoin
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# blog/storage.py
class BlogImageStorage(FileSystemStorage):
    location = os.path.join(settings.MEDIA_ROOT, "blog")
    base_url = urljoin(settings.MEDIA_URL, "blog/")

class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""
    location = os.path.join(settings.MEDIA_ROOT, "ckeditor5")
    base_url = urljoin(settings.MEDIA_URL, "ckeditor5/")