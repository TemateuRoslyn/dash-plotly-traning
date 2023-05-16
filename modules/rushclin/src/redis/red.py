from redis import Redis

redis = Redis(host="127.0.0.1", port=6379)
redis.ping()
redis.set("foo", "bar")
print(redis.get("foo"))
# redis = redis.StrictRedis(decode_responses=True)
# redis.ping()
