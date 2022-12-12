from redis import Redis

REDIS_HOST = ""
REDIS_PORT = ""
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)