import redis

conn = redis.Redis()
print(conn.keys('*'))

print(conn.set('secret', 'ni!'))
print(conn.set('carats', 24))
print(conn.set('fever', '101.5'))

print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))

print(conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!'))
print(conn.get('secret'))

print(conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!'))
print(conn.get('secret'))

print(conn.getrange('secret', -6, -1))

print(conn.setrange('secret', 0, 'ICKY'))
print(conn.get('secret'))

print(conn.mset({'pie': 'cherry', 'cordial': 'sherry'}))
print(conn.mget(['fever', 'carats']))

print(conn.delete('fever'))

print(conn.incr('carats'))
print(conn.incr('carats', 10))
print(conn.decr('carats'))
print(conn.decr('carats', 15))

print(conn.set('fever', '101.5'))
print(conn.incrbyfloat('fever'))
print(conn.incrbyfloat('fever', 0.5))
print(conn.incrbyfloat('fever', -2.0))

print(conn.lpush('zoo', 'bear'))
print(conn.lpush('zoo', 'alligator', 'duck'))
print(conn.linsert('zoo', 'before', 'bear', 'beaver'))
print(conn.linsert('zoo', 'after', 'bear', 'cassowary'))

print(conn.lset('zoo', 2, 'marmoset'))
print(conn.rpush('zoo', 'yak'))
print(conn.lindex('zoo', 3))
print(conn.lrange('zoo', 0, 2))
print(conn.ltrin('zoo', 1, 4))
print(conn.lrange('zoo', 0, -1))

print(conn.hmset('song', {'do': 'a deer', 're': 'about a deer'}))
print(conn.hset('song', 'mi', 'a note to follow re'))
print(conn.hget('song', 'mi'))
print(conn.hmget('song', 're', 'do'))
print(conn.hkeys('song'))
print(conn.hvals('song'))
print(conn.hlen('song'))
print(conn.hgetall('song'))
print(conn.hsetnx('song', 'fa', 'a note that rhymes with la'))

print(conn.sadd('zoo', 'duck', 'goat', 'turkey'))
print(conn.scard('zoo'))
print(conn.smembers('zoo'))
print(conn.srem('zoo', 'turkey'))
print(conn.sadd('better_zoo', 'tiger', 'wolf', 'duck'))
print(conn.sinter('zoo', 'better_zoo'))
print(conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo'))
print(conn.smembers('fowl_zoo'))
print(conn.sunion('zoo', 'better_zoo'))
print(conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo'))
print(conn.smembers('fabulous_zoo'))
print(conn.sdiff('zoo', 'better_zoo'))
print(conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo'))
print(conn.smembers('zoo_sale'))


import time
now = time.time()
print(now)

print(conn.zadd('logins', 'smeagol', now))
print(conn.zadd('logins', 'sauron', now+(5*60)))
print(conn.zadd('logins', 'bilbo', now+(2*60*60)))
print(conn.zadd('logins', 'treebeard', now+(24*60*60)))
print(conn.zrank('logins', 'bilbo'))
print(conn.zscore('logins', 'bilbo'))
print(conn.zrange('logins', 0, -1))
print(conn.zrange('logins', 0, -1, withscores=True))


import time

key = 'now you see it'
print(conn.set(key, 'but not for long'))
print(conn.expire(key, 5))
print(conn.ttl(key))
print(conn.get(key))
time.sleep(6)
print(conn.get(key))