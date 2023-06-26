# redis コンテナ起動方法

```bash
docker build -t my_redis .
docker run --rm --name my_redis_container -p 16379:6379 my_redis:latest
```
