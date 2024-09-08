python -u "/home/catalunha/apps/celery_redis_1/app/app.py"
celery-redis-1-py3.12catalunha@pop-os:~/apps/celery_redis_1$ python -u "/home/catalunha/apps/celery_redis_1/app/app.py"
Redis: Olá, $Word
Traceback (most recent call last):
  File "/home/catalunha/apps/celery_redis_1/app/app.py", line 5, in <module>
    a = hello_redis.delay("teste2")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/task.py", line 444, in delay
    return self.apply_async(args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/task.py", line 594, in apply_async
    return app.send_task(
           ^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/base.py", line 797, in send_task
    with self.producer_or_acquire(producer) as P:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/base.py", line 932, in producer_or_acquire
    producer, self.producer_pool.acquire, block=True,
              ^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/base.py", line 1354, in producer_pool
    return self.amqp.producer_pool
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/amqp.py", line 591, in producer_pool
    self.app.connection_for_write()]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/base.py", line 829, in connection_for_write
    return self._connection(url or self.conf.broker_write_url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/celery/app/base.py", line 880, in _connection
    return self.amqp.Connection(
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/kombu/connection.py", line 201, in __init__
    if not get_transport_cls(transport).can_parse_url:
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/kombu/transport/__init__.py", line 91, in get_transport_cls
    _transport_cache[transport] = resolve_transport(transport)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/kombu/transport/__init__.py", line 76, in resolve_transport
    return symbol_by_name(transport)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/kombu/utils/imports.py", line 59, in symbol_by_name
    module = imp(module_name, package=package, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/catalunha/.pyenv/versions/3.12.0/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1381, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1325, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 929, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 994, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/catalunha/apps/celery_redis_1/.venv/lib/python3.12/site-packages/kombu/transport/redis.py", line 267, in <module>
    class PrefixedStrictRedis(GlobalKeyPrefixMixin, redis.Redis):
                                                    ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'Redis'
celery-redis-1-py3.12catalunha@pop-os:~/apps/celery_redis_1$ poetry add redis
Using version ^5.0.8 for redis

Updating dependencies
Resolving dependencies... (0.1s)

Package operations: 1 install, 0 updates, 0 removals

  - Installing redis (5.0.8)

Writing lock file
celery-redis-1-py3.12catalunha@pop-os:~/apps/celery_redis_1$ python -u "/home/catalunha/apps/celery_redis_1/app/app.py"
Redis: Olá, $Word
23e3233a-67cf-4030-8f1d-f61bfeafc86b
celery-redis-1-py3.12catalunha@pop-os:~/apps/celery_redis_1$ 


subir do container do redis com
$ docker container run redis-local

catalunha@pop-os:~/apps/celery_redis_1/app$ poetry run celery -A tasks worker --loglevel=INFO


catalunha@pop-os:~/apps/celery_redis_1/app$ poetry run celery -A tasks worker --beat --loglevel=INFO
