from functools import reduce

assert(reduce(lambda x, y: x * y, [1, 2, 3, 4]) == 24)
print(reduce(lambda x, y: x * y, [num for num in range(100, 1000 + 1) if num % 2 == 0]))