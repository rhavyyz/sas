from numpy import log as ln
from math import ceil
import math


def abs(val: float):
    if val < 0:
        return val * (-1)

    return val


def dicotomia(precision: float, a: float, b: float):

    def func(x): return (x*x + 1.45 * x - 2.05)
    # def der(x): return x*x*3 - 2*x

    if func(b) < func(a):
        aux = b
        b = a
        a = aux

    cont = 0
    while (cont < 30):
        mid = b-a/2 + a

        fmid = func(mid)

        print(f'{cont + 1}: {fmid} | range {a} <-> {b} |  mid: {mid}')

        if abs(fmid) <= precision:
            break

        if fmid > 0:
            b = mid
        else:
            a = mid

        cont += 1


print('positiva')
dicotomia(0.0001, float(-0.725), float(2))

print('\n\n\n\nnegativa')
dicotomia(0.0001, float(-2.5), float(-0.725))
