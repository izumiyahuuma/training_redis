""" https://redis.io/docs/clients/python/ """
from redis import Redis

r: Redis = Redis(host='localhost', port=16379)
# 単純な保存
r.set('foo', 'bar')
print(r.get('foo'))

# dictの保存
r.hset('user-session:123', mapping={
    'name': 'John',
    'surname': 'Smith',
    'company': 'Redis',
    'age': 2
})
print(r.hgetall('user-session:123'))

# TODO : clusterは後回し
