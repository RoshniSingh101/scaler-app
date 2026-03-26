import os

class Config:
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    MEMCACHED_HOST = os.getenv('MEMCACHED_HOST', 'memcached')
    HOSTNAME = os.getenv('HOSTNAME', 'Unknown_Clone')