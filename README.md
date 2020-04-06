# envoy_with_redis

## Running 2 instance of redis with Envoy.

```bash
git clone git@github.com:CS2552F-DOSA/envoy_with_redis.git
```



### Run redis prod and redis test

```bash
# Run redis prod with envoy
cd envoy_with_redis/examples/redis_all
docker-compose pull
docker-compose up --build -d

```

### Redis connection

```bash
docker ps -a
```

![Screen Shot 2020-04-05 at 12.47.13 PM](img/Screen%20Shot%202020-04-05%20at%2012.47.13%20PM.png)

```bash
docker exec -it 898426e56711 bash
python client.py
```

![Screen Shot 2020-04-05 at 12.48.56 PM](img/Screen%20Shot%202020-04-05%20at%2012.48.56%20PM.png)

```bash
exit
```




### Stop redis prod and redis test

```bash
docker-compose down
```



### To use custom Envoy version

```bash
# change envoy docker images in 
envoy_with_redis/examples/redis_all/Dockerfile-backenvoy
envoy_with_redis/examples/redis_all/Dockerfile-frontenvoy

# then adjust the filter in yaml files
```



### Test the connectivity for redis test and redis prod

for test, uncomment the 

```
    # for debuging  
    # ports:
      # - "1999:1999"
      # - "8002:8002"
```

and 

```
# Test for redis prod with envoy
$ redis-cli -h localhost -p 1999 set foo foo
OK
$ redis-cli -h localhost -p 1999 set bar bar
OK
$ redis-cli -h localhost -p 1999 get foo
"foo"
$ redis-cli -h localhost -p 1999 get bar
"bar"

# Test for redis test with envoy
$ redis-cli -h localhost -p 1998 set foo foo-test
OK
$ redis-cli -h localhost -p 1998 set bar bar-test
OK
$ redis-cli -h localhost -p 1998 get foo
"foo-test"
$ redis-cli -h localhost -p 1998 get bar
"bar-test"
```

