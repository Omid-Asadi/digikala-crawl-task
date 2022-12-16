import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FORMAT = '[%(asctime)s]-[%(levelname)s]-[%(pathname)s]-[Line:%(lineno)s]-[%(message)s]'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': LOG_FORMAT
        },
        'simple': {
            'format': LOG_FORMAT
        },
    },
    'handlers': {
        'django_file': {
            'level': 'INFO',

            'class': 'logging.handlers.TimedRotatingFileHandler',
            'interval': 1,
            'when': 'midnight',

            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'formatter': 'simple'
        },
        'process_file': {
            'level': 'INFO',

            'class': 'logging.handlers.TimedRotatingFileHandler',
            'interval': 1,
            'when': 'midnight',

            'filename': os.path.join(BASE_DIR, 'logs', 'process_pay.log'),
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['django_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'process': {
            'handlers': ['process_file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
