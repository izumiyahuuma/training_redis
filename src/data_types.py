"""https://redis.io/docs/data-types/tutorial/ を pythonでやったもの"""
from redis import Redis
from connect_redis import connect
import time

r: Redis = connect()


def strings():
    print('### strings')
    r.set('mykey', 'somevalue')
    print(r.get('mykey'))

    # nx : keyが存在しない場合のみsetする
    # xx : keyが存在している場合のみsetする
    print(r.set('mykey', 'newval', nx=True))
    print(r.set('mykey', 'newval', xx=True))

    # インクリメント
    r.set('counter', 100)
    print(r.incr('counter'))
    print(r.incr('counter'))
    print(r.incrby('counter', 50))

    # 複数set,get
    r.mset({'a': 10, 'b': 20, 'c': 30})
    print(r.mget(['a', 'b', 'c']))  # 指定した順序でのvalueが返ってくる


def altering_and_quering_the_key_space():
    print('### Altering and querying the key space ###')

    # exist
    print(r.set('mykey', 'hello'))
    print(r.exists('mykey'))
    print(r.delete('mykey'))
    print(r.exists('mykey'))


def key_expiration():
    print('### Key expiration')
    # 有効期限の指定
    print(r.set('key', 'some-value', ex=5))
    print(r.get('key'))
    time.sleep(5)  # 5秒後に値取得できなくなる
    print(r.get('key'))
    print(r.ttl('key'))


if __name__ == "__main__":
    strings()
    altering_and_quering_the_key_space()
    key_expiration()
