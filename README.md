# Slow Django

> Django, but slower

Ever thought that your project was too fast?

## Install
```
pip install slow_django
```

```python
# settings.py

import slow_django

SLOW_MIN = 2 # Minimum page load in seconds
SLOW_MAX = 10 # Maximum-ish page load in seconds

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'slow_django.middleware.slowdown'
]
```