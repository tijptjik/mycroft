"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""

import logging

# To extend any settings from settings/base.py here's an example:
#from . import base
#INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django_login',
        'PASSWORD': 'fairview',
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'db/development.sqlite3',
        'HOST': '',
        'PORT': '',
        #'OPTIONS': {
        #    'init_command': 'SET storage_engine=InnoDB',
        #    'charset' : 'utf8',
        #    'use_unicode' : True,
        #},
        #'TEST_CHARSET': 'utf8',
        #'TEST_COLLATION': 'utf8_general_ci',
    },
    # 'slave': {
    #     ...
    # },
}

SITE_ID = 3
SITE_NAME = 'http://mycroftlectures.com'

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    ('Mart van de Ven', 'm@type.hk'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Hong_Kong'

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = PAYPAL_TEST = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'y4njob79%5m!1=pqj155=k$a04fa5r=icnb#2(t7v$_(%6iv2('


## Log settings

LOG_LEVEL = logging.DEBUG
HAS_SYSLOG = True
SYSLOG_TAG = "http_app_mycroft"  # Make this unique to your project.
# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'loggers': {
        'mycroft': {
            'level': "DEBUG"
        }
    }
}

# Common Event Format logging parameters
#CEF_PRODUCT = 'mycroft'
#CEF_VENDOR = 'Your Company'
#CEF_VERSION = '0'
#CEF_DEVICE_VERSION = '0'

INTERNAL_IPS = ('127.0.0.1')

# Enable these options for memcached
#CACHE_BACKEND= "memcached://127.0.0.1:11211/"
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY=True

# Set this to true if you use a proxy that sets X-Forwarded-Host
#USE_X_FORWARDED_HOST = False

if PAYPAL_TEST:
    PAYPAL_RECEIVER_EMAIL = "andy_1354358238_biz@type.hk"
else:
    PAYPAL_RECEIVER_EMAIL = "adbarker86@hotmail.com"

SUBSCRIPTION_PAYPAL_SETTINGS = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "notify_url": "%s%s" % (SITE_NAME, '/subscription/paypal/'),
        "return_url": "%s%s" % (SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (SITE_NAME, '/cancel/'),
    }



