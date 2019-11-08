import redis


r = redis.Redis(host='localhost', port=6379, db=0)

counter = 0
for i in range(0,5):
    temp = f'foo'
    r.set(temp,(counter + counter))
    counter += 1


print(r.get('foo'))