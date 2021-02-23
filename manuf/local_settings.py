# Email设置

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.263.net'
EMAIL_HOST_USER='manuf-tech@xfsunrise.com'
EMAIL_HOST_PASSWORD='Xyds123456,.'
EMAIL_PORT = 25
EMAIL_USE_TLS = True


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'manuf',
        'USER':'root',
        'PASSWORD':'usbw',
        'HOST':'127.0.0.1',
        'PORT':'3307',
        'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci;' }
        }
}

# Django-redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": "utf-8"
            },
             "PASSWORD": 'test123'
        }
    }
}


# SMS配置
SMS_APP_ID = 'AC6e670678aebb913331fc784a3256031d'
SMS_APP_KEY = '83aba864d7bdf92bf9a515edab6944f1'
