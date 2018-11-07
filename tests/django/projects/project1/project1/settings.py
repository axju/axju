import os

ALLOWED_HOSTS = ['test.de']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }
}
