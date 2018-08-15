#coding=utf-8
"""
Django settings for ftasomc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,datetime
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=98lc@ltbsrs*-d-!k#o*45_p!gxevu@2aa+j-un*mf3f%yeui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'session_security',
    'ops',
    'asset',
    'ansibleweb',
    'ansiblewebapp',
    'cobblerweb',
    'logs',
    'monitor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'ftasomc.urls'

WSGI_APPLICATION = 'ftasomc.wsgi.application'

DEBUG_TOOLBAR_CONFIG = {  'JQUERY_URL' : r"http://code.jquery.com/jquery-2.1.1.min.js"}
INTERNAL_IPS = ('*',)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'ansiblewebapp': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'AnsibleWebApp/db/ansible_web.db'),
    },
    'cobbler_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cobblerdb.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = (
    'static',
)

MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/static/media/'

DOCUMENT_URL = '/uploads/'
DOCUMENT_ROOT = '/uploads/'

# salt result

RETURNS_MYSQL = {
    'salt': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'salt',    #database name
        'USER': 'root',   #username
        'PASSWORD': 'root', #passwd
        'HOST': '127.0.0.1', #localhost
        'PORT': '3306', #mysql port
    }
}
# salt-api setting
SALT_API = {
        'url' : 'http://127.0.0.1:8888/',
        'user' : 'saltapi',
        'password' : 'saltapi'
        }
        
# ansible api
SITE_ID = 1
WORKER_TIMEOUT = 5 * 60
NUMBER_OF_TASK_PER_PAGE = 25
ANSIBLE_FORKS = 30
ANSIBLE_INVENTORY = '/etc/ansible/hosts'

# cobbler api
Cobbler_API = {"url": "",
            "user": "",
            "password": ""
            }
        
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
                'format': '%(asctiome)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d%(message)s'
                }
    },
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


########  ops ########
LOGIN_URL = '/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MaxTaskProcesses = 4
MultiTaskScript = '%s/%s'%(BASE_DIR,'backend/multitask.py')

RSA_PRIVATE_KEY_FILE = '%s/%s'%(BASE_DIR,'var/rsa_key/id_rsa')


Welcome_msg = '''
|-------\033[32;1m[Welcome login OMC Auditing System]\033[0m-----|
|            Version :   1.0                         |
|----------------------------------------------------|\n\n'''


FileUploadDir = 'upload'

SHELLINABOX = {
    'host':'localhost', #把’localhost‘替换成你的Shellinabox服务的启动IP
    'port':4200,
    'username':'crazy_audit', #你之前创建的crazy_audit账户,(这个账户相当于公共账户,从web页面登录webssh时会自动帮你填写)
    'password': 'root'    #账户密码
}

########  Django Suit ########
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'OMC管理后台',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
     'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)