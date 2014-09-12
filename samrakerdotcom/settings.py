# Django settings for samrakerdotcom project.
import os

import dj_database_url

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
TEMPLATE_DEBUG = DEBUG
VERSION = 'local'
ROOT = "."
#ROOT = "/Users/samuelraker/PycharmProjects/public/"
if VERSION == 'local':
    DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Sam Raker', 'sam.raker@gmail.com'),
)

MANAGERS = ADMINS
DATABASES = {"default": dj_database_url.config(default='postgres://rrjogyaikaudpd:q6MoyO8SVLLe09BKoK4XqqNT-8@ec2-54-225-124-205.compute-1.amazonaws.com:5432/dec2im2qmts9c9')}


def get_cache():
    import os

    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS'].replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
        return {'default': {'BACKEND': 'django_pylibmc.memcached.PyLibMCCache', 'TIMEOUT': 500, 'BINARY': True,
                            'OPTIONS': {'tcp_nodelay': True}}}
    except:
        return {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}


CACHES = get_cache()


if VERSION == "production":
    CACHES["LOCATION"] = "127.0.0.1:8080"

ALLOWED_HOSTS = [".asecondtaste.net", ".samraker.com", 'localhost']

# if not DEBUG:
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 3

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
if VERSION == 'production':
    MEDIA_URL = 'http://www.samraker.com/media/'
else:
    MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = "staticfiles"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(ROOT, "static")),
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'app_namespace.Loader', 'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader', 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'samrakerdotcom.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'samrakerdotcom.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(ROOT, "static", "templates")),
    os.path.abspath(os.path.join(ROOT, "staticfiles", "templates")),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth', 'django.core.context_processors.i18n',
    'django.core.context_processors.media', 'django.core.context_processors.request',
    'django.core.context_processors.static', 'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    #'zinnia.context_processors.version'
)

INSTALLED_APPS = (
    'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.sites',
    'django.contrib.messages', 'django.contrib.staticfiles', # Uncomment the next line to enable the admin:
    'django.contrib.admin', # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs', 'samrakerdotcom', 'django.contrib.flatpages', 'django.contrib.humanize',
    'django.contrib.syndication', 'storages', 'bootstrap3')

#DISQUS_USER_API_KEY = secret.DISQUS_USER_API_KEY
#DISQUS_FORUM_SHORTNAME = 'samrakerdotcom'

BOOTSTRAP_BASE_URL = os.path.join(STATIC_URL, 'bootstrap/')
BOOTSTRAP_CSS_BASE_URL = os.path.join(BOOTSTRAP_BASE_URL, 'css/')
BOOTSTRAP_JS_BASE_URL = os.path.join(BOOTSTRAP_BASE_URL, 'js/')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sam.raker@gmail.com'
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]

#ZINNIA_MARKUP_LANGUAGE = 'restructuredtext'
## ZINNIA_USE_TWITTER = True
#TWITTER_CONSUMER_KEY = secret.TWITTER_CONSUMER_KEY
#TWITTER_CONSUMER_SECRET = secret.TWITTER_CONSUMER_SECRET
#TWITTER_ACCESS_KEY = secret.TWITTER_TOKEN
#TWITTER_ACCESS_SECRET = secret.TWITTER_TOKEN_SECRET
#
#ZINNIA_SPAM_CHECKER_BACKENDS = (
#    'zinnia.spam_checker.backends.long_enough', 'zinnia.spam_checker.backends.mollom',
#    'zinnia.spam_checker.backends.automattic',
#)
#MOLLOM_PUBLIC_KEY = secret.MOLLOM_PUBLIC_KEY
#MOLLOM_PRIVATE_KEY = secret.MOLLOM_PRIVATE_KEY
#AKISMET_SECRET_API_KEY = secret.AKISMET_SECRET_API_KEY
#ZINNIA_AUTO_MODERATE_COMMENTS = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {'version': 1, 'disable_existing_loggers': False, 'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
           'handlers': {'mail_admins': {'level': 'ERROR', 'filters': ['require_debug_false'], 'class': 'django.utils.log'
                                                                                                       '.AdminEmailHandler'}},
           'loggers': {'django.request': {'handlers': ['mail_admins'], 'level': 'ERROR', 'propagate': True, }, }}
