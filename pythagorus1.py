import math

print('This program will find all the right-angled triangles with sides a and b from 1 to 100')

for a in range(1, 101):
    for b in range(1, 101):
        c_squared = (a * a) + (b * b)
        c = math.sqrt(c_squared)
        if c.is_integer():
            print('%d² + %d² = %d²' % (a, b, c))
