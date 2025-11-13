import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Secret keys
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables.")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-jwt-secret-key")
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set in the environment variables.")


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
# Debug mode
# DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
DEBUG = True
# Allowed hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "http://localhost").split(",")

# CORS
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CORS_ALLOW_ALL_ORIGINS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'import_export',
    'django_ckeditor_5',
    'core',
    'blog',
]

MIDDLEWARE = [
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}



# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# SWAGGER
SPECTACULAR_SETTINGS = {
    'TITLE': 'ibc-blog API Documentation',
    'DESCRIPTION': 'API documentation for ibc-blog shopping store',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    },
}
# Internationalization
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", 'en-us')
TIME_ZONE = os.getenv("TIME_ZONE", 'UTC')
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static and Media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CK-EDITOR
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files"),
]
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "ckeditor_5": {"BACKEND": "blog.storage.CustomStorage"},# For CKEditor 5
    "blog_images": {"BACKEND": "blog.storage.BlogImageStorage"},  # For ImageField
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
CKEDITOR_5_FILE_STORAGE = "blog.storage.CustomStorage"
customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]
CKEDITOR_5_ALLOW_ALL_FILE_TYPES = True
CKEDITOR_5_CONFIGS = {
    "default": {
        "removePlugins": ["WordCount"],
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    "comment": {
        "language": {"ui": "en", "content": "ar"},
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    "extends": {
        "language": "en",
        "toolbar": {
            "items": [
                "heading",
                "|",
                "bold",
                "italic",
                "underline",
                "strikethrough",
                "highlight",
                "|",
                "bulletedList",
                "numberedList",
                "todoList",
                "blockQuote",
                "|",
                "link",
                "insertImage",
                "insertTable",
                "mediaEmbed",
                "codeBlock",
                "|",
                "fontSize",
                "fontFamily",
                "fontColor",
                "fontBackgroundColor",
                "|",
                "horizontalLine",
                "specialCharacters",
                "style",
                "sourceEditing",
                "removeFormat",
                "findAndReplace",
            ],
            "shouldNotGroupWhenFull": True,
        },
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
                "toggleTableCaption",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraph", "class": "ck-heading_paragraph"},
                {"model": "heading1", "view": "h1", "title": "Heading 1", "class": "ck-heading_heading1"},
                {"model": "heading2", "view": "h2", "title": "Heading 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Heading 3", "class": "ck-heading_heading3"},
            ],
        },
        "list": {
            "properties": {
                "styles": True,
                "startIndex": True,
                "reversed": True,
            },
        },
        "link": {"defaultProtocol": "https://"},
        "htmlSupport": {
            "allow": [
                {"name": "/.*/", "attributes": True, "classes": True, "styles": True},
            ],
        },
        "mention": {
            "feeds": [
                {
                    "marker": "@",
                    "feed": [
                        "@Barney",
                        "@Lily",
                        "@Marry Ann",
                        "@Marshall",
                        "@Robin",
                        "@Ted",
                    ],
                    "minimumCharacters": 1,
                },
            ],
        },
        "style": {
            "definitions": [
                {"name": "Article category", "element": "h3", "classes": ["category"]},
                {"name": "Info box", "element": "p", "classes": ["info-box"]},
            ],
            "uploadUrl": "/image_upload/"
        },

        "fontSize": {
            "options": [
                "tiny",
                "small",
                "default",
                "big",
                "huge",
            ],
        },
        "fontFamily": {
            "options": [
                "default",
                "Arial, Helvetica, sans-serif",
                "Georgia, serif",
                "Times New Roman, Times, serif",
                "Verdana, Geneva, sans-serif",
            ],
        },
        "fontColor": {
            "colors": customColorPalette,
        },
        "fontBackgroundColor": {
            "colors": customColorPalette,
        },
    },
}

CKEDITOR_5_CUSTOM_CSS = "custom.css"
CSRF_COOKIE_NAME = "new_csrf_cookie_name"
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "allow"