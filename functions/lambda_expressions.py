"""
 A single use and anonymous (no name)
"""

from functools import reduce

base_list = [1, 2, 3]

print(list(map(lambda item: item * 2, base_list)))

print(list(filter(lambda item: item % 2 != 0, base_list)))

print(reduce(lambda acc, item: acc + item, base_list, 0))

base_list = [5, 4, 3]

print(list(map(lambda item: item * item, base_list)))

list_sorting = [(0, 2), (4, 3), (10, -1), (9, 9)]
list_sorting.sort(key=lambda x: x[1])
print(list_sorting)
