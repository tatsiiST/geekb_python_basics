def fact(n):

    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


if __name__ == '__main__':
    from math import factorial

    for num, el in enumerate(fact(8), 1):
        assert (el == factorial(num))
        print(f'!{num} is {el}')