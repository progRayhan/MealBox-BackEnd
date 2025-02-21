from meal_box.settings.base_settings import *

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "0.0.0.0",
]

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "RESULTS_CACHE_SIZE": 3,
    "SHOW_COLLAPSED": True,
    "SQL_WARNING_THRESHOLD": 100,  # milliseconds
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
