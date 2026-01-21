from redis import Redis
from rq import Queue


# vou deixar fixado por enquanto
redis_url = "redis://redis:6379"
redis_conn = Redis.from_url(redis_url)
fila = Queue(connection=redis_conn)
