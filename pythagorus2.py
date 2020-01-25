import math

print('This program will find all the right-angled triangles with sides a and b from 1 to 100')

count = 0
for a in range(1, 101):
    for b in range(1, a):
        c_squared = (a * a) + (b * b)
        c = math.sqrt(c_squared)
        if c.is_integer():
            print('%d² + %d² = %d²' % (a, b, c))
            count += 1

print('There are %d solutions' % count)
