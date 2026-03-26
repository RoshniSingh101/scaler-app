import redis
from config import Config

class CacheService:
    def __init__(self):
        self.r = redis.Redis(host=Config.REDIS_HOST, port=6379, decode_responses=True)

    def increment_hits(self):
        return self.r.incr("hits")

cache_service = CacheService()