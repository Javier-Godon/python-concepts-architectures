from functools import reduce

input_list = [1, 2, 3]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, input_list, 0))
