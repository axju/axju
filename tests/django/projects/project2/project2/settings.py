import os

HOST = 'test.de'

ALLOWED_HOSTS = [HOST]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }
}
