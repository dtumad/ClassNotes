#Algorithm for calculating fundamental unit in a real quadratic field
from math import sqrt
def is_square(n):
    if int(sqrt(n))**2 == n:
        return int(sqrt(n))
    return None

def is_square_free(n):
    for i in range(2,int(n/2) + 1):
        if n % i == 0 and (n / i) % i == 0:
            return False
    return True

def calc_unit(m):
    if m % 4 == 0:
        return '-1'
    if m % 4 == 3 or m % 4 == 2: k = 1
    else: k = 4
    a, b = None, 0
    while a == None:
        b += 1
        a = is_square(m * b * b + k)
    return "{} + {}*sqrt({})".format(a, b, m)

for i in range(2,31):
    if is_square_free(i):
        print(str(i) + " -> " + calc_unit(i))
            
