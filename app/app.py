from tasks import hello_redis

# a = hello_redis("Word1")
# print(a)
print("inicio")
a = hello_redis.delay("teste6")
print("fim")
print(a)
