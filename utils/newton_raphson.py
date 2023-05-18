import math


def abs(val: float):
    if val > 0:
        return val

    return -val


def newton_raphson(precision: float, x, func, deriv):

    while abs(func(x)) > precision:
        # print(x, '  func: ', func(x), ' - deriv: ', deriv(x))
        print('-=' * 40)

        print(f'x: {x}')
        print(f'func: {func(x)}')
        print(f'deriv: {deriv(x)}')

        print('-=' * 40)

        x -= func(x)/deriv(x)
    print(x)
    print('\n\n\n\n')


print('\nq1')
newton_raphson(
    precision=0.0001,
    x=7/float(2),
    func=lambda x: x * x - 7,
    deriv=lambda x: 2 * x
)
print('\nq2')
newton_raphson(
    precision=0.001,
    x=2.3,
    func=lambda x: math.pow(x - 2, 4),
    deriv=lambda x:  math.pow(x - 2, 3) * 4
)
print('\nq3')
newton_raphson(
    precision=0.001,
    x=1,
    func=lambda x: math.pow(math.e, x) - x * x,
    deriv=lambda x:  math.pow(math.e, x) - 2 * x
)
print('\nq4')
newton_raphson(
    precision=0.001,
    x=0.5,
    func=lambda x: x * math.sin(x),
    deriv=lambda x:  math.sin(x) + x * math.cos(x)
)
print('\nq5')
print('a')
newton_raphson(
    precision=0.001,
    x=3,
    func=lambda x: x * x - 8,
    deriv=lambda x:  2 * x
)
print('b')
newton_raphson(
    precision=0.001,
    x=7,
    func=lambda x: x * x - 91,
    deriv=lambda x:  2 * x
)
print('c')
newton_raphson(
    precision=0.001,
    x=3,
    func=lambda x: x * x * x - 7,
    deriv=lambda x:  3 * x * x
)
print('d')
newton_raphson(
    precision=0.001,
    x=10,
    func=lambda x: x * x * x - 200,
    deriv=lambda x:  3 * x * x
)


# newton_raphson(
#     precision=0.001,
#     x=10,
#     func=lambda x: math.pow(math.e, x) - x * x,
#     deriv=lambda x:  math.pow(math.e, x) - 2 * x
# )
