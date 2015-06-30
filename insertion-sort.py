import random
a = [int(random.uniform(1, 50)) for i in xrange(10)]
print a
for i in xrange(len(a)):
    if i > 0:
        while a[i-1] >= a[i] and i > 0:
            a[i-1], a[i] = a[i], a[i-1]
            i = i-1
print a