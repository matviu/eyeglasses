# -*- coding: utf-8 -*-
"""
Django settings for eyeglasses project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^024r8&r_a*-fgcv#=orvv0&(hwv4k_@u!15nj#6wk@km#yx6q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'pages',
    'chunks',
    'catalog',
    'eyeglasses.custom_catalog',
    'feedback',
    'eyeglasses.custom_feedback',
    'tinymce',
    'attachment',
    'eyeglasses.custom_attachment',
    'imagekit',
    'seo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eyeglasses.urls'

WSGI_APPLICATION = 'eyeglasses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'

STATICFILES_DIRS = (
    BASE_DIR + '/eyeglasses/static/',
)



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media/'

# Templates

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "pages.context_processors.media",
    'django.core.context_processors.static',
)


# caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'eyeglasses',
        'OPTIONS': {
            'MAX_ENTRIES': 500
        }
    }
}



# page-cms

PAGE_DEFAULT_TEMPLATE = 'pages/frontpage.html'

PAGE_TEMPLATES = (

)

gettext_noop = lambda s: s

# languages you want to translate into the CMS.
PAGE_LANGUAGES = (
    ('ru', gettext_noop('Russian')),
)

PAGE_TINYMCE = True

# attachments

ATTACHMENT_FOR_MODELS = [
    'pages.models.Page',
    'eyeglasses.custom_catalog.models.Section',
    'eyeglasses.custom_catalog.models.Eyeglasses'
]

ATTACHMENT_LINK_MODELS = [
    'pages.models.Page',
    'eyeglasses.custom_catalog.models.Section',
    'eyeglasses.custom_catalog.models.Eyeglasses'
]

TINYMCE_DEFAULT_CONFIG = {
    'mode': 'exact',
    'theme': 'advanced',
    'relative_urls': False,
    'width': 820,
    'height': 500,
    'content_css': '%scss/tinymce.css' %STATIC_URL,
    'skin': 'o2k7',
    'plugins': 'table,advimage,advlink,inlinepopups,preview,media,searchreplace,contextmenu,paste,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras',
    'theme_advanced_buttons1': 'justifyleft,justifycenter,justifyright,|preview,fullscreen,|,bold,italic,underline,strikethrough,|,sub,sup,|,bullist,numlist,|,outdent,indent,|,formatselect,removeformat,cut,copy,paste,pastetext,pasteword,|,search,replace,|,undo,redo,|,link,unlink,anchor,image,media,charmap,|,visualchars,nonbreaking',
    'theme_advanced_buttons2': 'visualaid,tablecontrols,|,blockquote,del,ins,|,code',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'extended_valid_elements': 'b,i,noindex,iframe[id|src|width|height|frameborder|webkitallowfullscreen|mozallowfullscreen|allowfullscreen]',
    'custom_elements': 'noindex',
    'external_image_list_url': 'images/',
    'external_link_list_url': 'links/',
    'paste_remove_styles': 'true',
    'paste_remove_styles_if_webkit': 'true',
    'paste_strip_class_attributes': 'all',
    'plugin_preview_width': '900',
    'plugin_preview_height': '800',
    'accessibility_warnings': 'false',
}

TINYMCE_JS_URL = '%stiny_mce/tiny_mce.js' % STATIC_URL
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'tiny_mce')
TINYMCE_COMPRESSOR = False

ATTACHMENT_IKSPECS = 'eyeglasses.custom_attachment.ikspecs'
ATTACHMENT_SPECS_FOR_TINYMCE = ['wdisplay', ]

# seo

SEO_FOR_MODELS = [
    'pages.models.Page',
    'eyeglasses.custom_catalog.models.Section',
    'eyeglasses.custom_catalog.models.Eyeglasses',
]

# catalog

CATALOG_MODELS = (
    'custom_catalog.Section',
    'custom_catalog.Eyeglasses',
)

# feedback

FEEDBACK_FORMS = {
    # 'consult': 'eidvery.custom_feedback.forms.ConsultForm',
    # 'zamer': 'eidvery.custom_feedback.forms.ZamerForm',
    # 'zayavka': 'eidvery.custom_feedback.forms.ZayavkaForm',
}
FEEDBACK_PREFIX_KEY_FIELDS = True
FEEDBACK_FORMS_NAMES = {
    # 'consult': u'Получить консультацию',
    # 'zamer': u'Вызвать замерщика',
    # 'zayavka': u'Отправить заявку',
}