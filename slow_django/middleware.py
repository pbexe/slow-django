import time
import random
from django.conf import settings


def slowdown(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        
        try:
            max_ = settings.SLOW_MAX
        except NameError:
            max_ = 5
        
        try:
            min_ = settings.SLOW_min
        except NameError:
            min_ = 2
        time.sleep(random.randint(min_,max_))
        return response

    return middleware