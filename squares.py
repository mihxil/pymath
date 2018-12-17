#!/usr/bin/env python3

import itertools
import sys


# works in any base, for bases > 10 it may become a bit slow..
if len(sys.argv) > 1:
    base=int(sys.argv[1])
else:
    base=10

print("Showing in base " + str(base))

def number(digits: list):
    result = 0
    pow = 1
    for d in reversed(digits):
        result += d * pow
        pow *= base
    return result


# Newton's method works perfectly well on integers:
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def number_to_base(number: int):
    alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
    result = ""
    while number > 0:
        number,idx = divmod(number, base)
        result = alphabet[idx] + result
    return result


for i in range(1, base):
    print(i)
    for perm in list(itertools.permutations(range(1, i + 1))):
        n = number(list(perm))
        isq = isqrt(n)
        if isq ** 2 == n:
            print("\t" + number_to_base(n) + "\t=" + number_to_base(isq) + "*" + number_to_base(isq))

