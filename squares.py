#!/usr/bin/env python3

import itertools
import sys


# works in any base, for bases > 10 it may become a bit slow..
if len(sys.argv) > 1:
    base = int(sys.argv[1])
else:
    base = 10

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


def number_to_base(n: int):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    while n > 0:
        n, idx = divmod(n, base)
        result = digits[idx] + result
    return result


for i in range(1, base):
    print(number_to_base(i))
    for perm in list(itertools.permutations(range(1, i + 1))):
        n = number(list(perm))
        iroot = isqrt(n)
        if iroot ** 2 == n:
            if base != 10:
                print("\t%s (%d)\t= %s² (%d²)" % (number_to_base(n), n,  number_to_base(iroot), iroot))
            else:
                print("\t%d\t= %d²" %  (n, iroot))


