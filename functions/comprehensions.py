"""
comprehensions
"""

'''
*******************List***************************************
'''

base_list = []
for char in 'comprehensions':
    base_list.append(char)

print(base_list)

'''
with comprehensions
'''

base_list = [char for char in 'comprehensions']
print(base_list)

base_list = [num for num in range(0, 100)]
print(base_list)

base_list = [num * 2 for num in range(0, 100)]
print(base_list)

base_list = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(base_list)

base_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
no_duplicates_set = set([char for char in base_list])
duplicates_list = list(set([char for char in base_list if base_list.count(char) > 1]))
print(no_duplicates_set)
print(duplicates_list)

'''
*******************Set***************************************
'''

print("*****************set**********************************")

base_set = {char for char in 'comprehensions'}
print(base_set)

base_set = {num for num in range(0, 100)}
print(base_set)

base_set = {num * 2 for num in range(0, 100)}
print(base_set)

base_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(base_set)

'''
*******************dictionary***************************************
'''

print("*****************dictionary**********************************")

simple_dict = {
    'first key': 11,
    'second key': 23,
    'third key': 30,
    'fourth key': 12
}

base_dic = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(base_dic)

base_dic = {num: num * 2 for num in [1, 2, 3]}
print(base_dic)
