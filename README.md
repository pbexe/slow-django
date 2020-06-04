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
    # ...
    'slow_django.middleware.slowdown'
]
```
