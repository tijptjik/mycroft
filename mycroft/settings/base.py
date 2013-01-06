"""
This is your project's main settings file that can be committed to your
repo. If you need to override a setting locally, use local.py
"""

import os
#import memcache_toolbar.panels.memcache

# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")

# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'base_css': (
            'css/style.css',
        ),
    },
    'js': {
        'libs_js': (
            'js/libs/jquery-1.6.2.min.js',
            'js/libs/modernizr-2.0.6.min.js',
        ),
    }
}

SUPPORTED_NONLOCALES = ['media', 'admin', 'static']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Defines the views served for root URLs.
ROOT_URLCONF = 'mycroft.urls'

INSTALLED_APPS = [
    
    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    # 'commonware.response.cookies',
    # 'session_csrf',
    'debug_toolbar',
    'compressor',
    #'debug_toolbar_user_panel',
    #'memcache_toolbar',

    # Database migrations
    'south',

    # Registration
    'registration',
    'registration_email',
    'registration_touch',
    
    # Transactions
    'paypal.standard.ipn',
    'subscription',

    # Application base, containing global templates.
    'mycroft.base',
    'gunicorn',
    'django_extensions',
    'djsupervisor',
]

# Place bcrypt first in the list, so it will be the default password hashing
# mechanism
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# Sessions
#
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = False

# Set this to true if you are using https
SESSION_COOKIE_SECURE = False

## Tests
TEST_RUNNER = 'test_utils.runner.RadicalTestSuiteRunner'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.example.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.example.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'commonware.middleware.FrameOptionsHeader',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'mycroft.base.disable.DisableCSRF', 
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

COMPRESS_PRECOMPILERS = (
   ('text/less', 'lesscpy {infile} {outfile}'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

def custom_show_toolbar(request):
    """ Only show the debug toolbar to users with the superuser flag. """
    return request.user.is_superuser

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}

DEBUG_TOOLBAR_PANELS = (
    #'debug_toolbar_user_panel.panels.UserPanel',
    #'memcache_toolbar.panels.memcache.MemcachePanel',
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

FILE_UPLOAD_PERMISSIONS = 0664

INTERNAL_IPS = ('127.0.0.1',)

SITE_NAME = 'http://mycroftlectures.com'

PAYPAL_RECEIVER_EMAIL = "andy_1354358238_biz@type.hk"

SUBSCRIPTION_PAYPAL_SETTINGS = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "notify_url": "%s%s" % (SITE_NAME, '/subscription/paypal/'),
        "return_url": "%s%s" % (SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (SITE_NAME, '/cancel/'),
    }

PAYPAL_TEST = True

ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
    'registration_email.auth.EmailBackend',
)

LOGIN_REDIRECT_URL = '/'

DEFAULT_FROM_EMAIL = 'Andrew Barker <andrew.barker@mycroft-online-lectures.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'andrew.barker@mycroft-online-lectures.com'
EMAIL_HOST_PASSWORD = 'hisdarkmaterials'
EMAIL_PORT = 587

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ANON_ALWAYS = True

DOWNLOAD_EXPIRATION_DAYS = 14

USE_XSENDFILE = True

# The WSGI Application to use for runserver
WSGI_APPLICATION = 'mycroft.wsgi.application'
