# Two options: normal redis client and asyncio-redis

REDIS_HOST = "redis-proxy"
REDIS_PORT = "1999"

REDIS_TEST_HOST = "redis-test-proxy"
REDIS_TEST_PORT = "1999"

# Normal redis client
# Referring to https://redislabs.com/lp/python-redis/

import redis
import os
import time

# the prod redis is with the prefix redis:
# the test redis is with the prefix redis-test:

print("\n************* client begin *************\n")

# test for connection for prod redis

r = redis.Redis(
    host= REDIS_HOST,
    port= REDIS_PORT)
print("set foo in redis, foo -> bar redis")
r.set('foo', 'bar redis')
value = r.get('foo')
print("getted value for foo in redis: ", value)
print("\n\n")

print("---------------------------------------------")
time.sleep(0.5)

# test for connection for test redis

r_test = redis.Redis(
    host= REDIS_TEST_HOST,
    port= REDIS_TEST_PORT)
print("set foo in redis-test, foo -> bar redis-test")
r_test.set('foo', 'bar redis-test')
value = r_test.get('foo')
print("getted value for foo in redis: ", value)



print("\n************* client end *************\n")
time.sleep(0.5)