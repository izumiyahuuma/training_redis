from redis import Redis


def connect() -> Redis:
    r: Redis = Redis(host='localhost', port=16379)
    return r
