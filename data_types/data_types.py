# Fundamentals

integer: int
a_float: float
boolean: bool
string: str
a_list: list
my_tuple: tuple
a_set: set
dictionary: dict

# Classes -> custom types

# Specialized Data Types: packages and modules we can use from libraries

long_string = '''
this is
a long string
I can write in 
multiple lines
'''

print(long_string)
print(str(100))

# Escape sequence \
print('It\'s \'kind of\' \nsunny')

name = 'Javier'
surname = 'Brown'
print(f'hello {name} {surname}')
print('hello {name} {surname}'.format(name='Javier', surname='Brown'))
print('hello {} {}'.format('Javier', 'Brown'))
print('hello {} {}'.format(name, surname))
print('hello {1} {0}'.format('Javier', 'Brown'))

introduction = 'allow me introduce myself'
print(introduction[9:25])
print(introduction[9:])
print(introduction[:9])
print(introduction[::-1])  # reverse of the string

# Built-in functions: https://docs.python.org/3/library/functions.html
print(len(introduction))

# Methods: are similar to functions but owned by something (EX: String methods -> actions that only strings can perform)
print(introduction.upper())
print(introduction.find('introduce'))
print(introduction.replace('allow me', 'I will'))

print(f'boolean of 0 is {bool(0)}')
print(f'boolean of 1 is {bool(1)}')

# birth_year = input('What is your birth?')
#
# age = datetime.date.today().year - int(birth_year)
# print(f'your age is: {age}')

'''
lists (they are mutable)
'''
my_cart = ['notebook', 'phone', 'globes', 'books', 'pen', 'pencil', 'toys', 'grapes']
print(my_cart[0])
print(my_cart[-1])
print(my_cart[0:2])
print(my_cart[0::2])
my_cart[0] = 'modified'
print(my_cart)
new_cart = my_cart
new_cart[0] = 'modified in copy'
print(my_cart)
print(new_cart)
# but if I do slicing I create an individual copy !!!!!!!!!!!!!!!!!!!!!!
my_cart = ['notebook', 'phone', 'globes', 'books', 'pen', 'pencil', 'toys', 'grapes']
new_cart_with_slicing = my_cart[:]
new_cart_with_slicing[0] = 'modified in copy'
print(my_cart)
print(new_cart_with_slicing)

# Matrix: multidimensional list
matrix = [
    ['notebook', 'phone', 'globes', 'books', 'pen', 'pencil', 'toys', 'grapes'],
    ['second notebook', 'second phone', 'second globes', 'second books', 'second pen', 'second pencil', 'second toys',
     'second grapes'],
    ['third notebook', 'third phone', 'third globes', 'third books', 'third pen', 'third pencil', 'third toys',
     'third grapes']
]
print(matrix[1][0])
print(len(matrix))
print(len(matrix[0]))
matrix[0].append('appended')
print(matrix[0])
matrix[0].append(str(100))
print(matrix[0])
matrix[0].insert(4, '**INSERTED**')
print(matrix[0])
matrix[1].extend(['extended1', 'extended2'])
print(matrix[1])
matrix[1].pop()
print(matrix[1])
matrix[1].pop(4)
print(matrix[1])
matrix[2].remove('third grapes')
print(matrix[2])

new_list = matrix[2].remove('third toys')  # remove does not return a value
print(new_list)

new_list = matrix[2].pop()  # pop returns the value that is removed
print(new_list)
matrix[2].clear()  # removes whatever is in the list
print(matrix[2])

print(matrix[0].index('globes'))

print('globes' in matrix[0])
print('not' in matrix[0])
matrix[0].sort()  # sorts the original array
print(matrix[0])
print(sorted(matrix[1]))
# sorted produces a new array (creates a copy and sorts it)
# it is like doing:
new_list_from_matrix1 = matrix[1]
new_list_from_matrix1.sort()
print(new_list_from_matrix1)
matrix[1].reverse()
print(matrix[1])
print(matrix[1][::-1])  # same as reverse

range_list = list(range(1, 50))
print(range_list)

sentence = ''
sentence.join(['Hi', ' my', ' name', ' is', ' Javier'])
print(sentence)
new_sentence = sentence.join(['Hi', ' my', ' name', ' is', ' Javier'])  # It is creating a new sentence
print(new_sentence)
sentence = '*'
new_sentence = sentence.join(['Hi', ' my', ' name', ' is', ' Javier'])  # It is creating a new sentence
print(new_sentence)

new_sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Javier'])
print(new_sentence)

'''
list unpacking
'''

a, b, c = ['notebook', 'phone', 'globes']
print(a)
print(b)
print(c)

a, b, c, *other, d = ['notebook', 'phone', 'globes', 'books', 'pen', 'pencil', 'toys', 'grapes']
print(other)
print(d)

'''
DICTIONARY: Unordered key,value pair
a key needs to be immutable (it uses HASH algorithm to search for elements)
'''
dictionary = {'a': 'notebook',
              'b': ['second notebook', 'second phone', 'second globes', 'second books', 'second pen', 'second pencil',
                    'second toys',
                    'second grapes'], 'c': 'globes'}
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['b'][2])

# print(dictionary['not found']) -> throws an error and interrupts the execution of the program
print(dictionary.get('not found'))  # get manages the error and returns None is the key is not found
print(dictionary.get('not found', 'key not found'))

dictionary = dict(a='notebook', b='second notebook', c='second globes')
dictionary.update({'d': 'new item'})
print(dictionary)
print(dictionary.get(a, 'input key is not a string'))
print(dictionary.get('a'))

print(a in dictionary)
print('a' in dictionary)
print('notebook' in dictionary)
print('notebook' in dictionary.keys())
print('notebook' in dictionary.values())
print(dictionary.items())

print(
    dictionary.popitem())  # randomly pops something. From Python 3.7 removes the last key:value pair that was inserted
print(dictionary)
print(dictionary.pop('a'))
print(dictionary)

'''
TUPLE
Unlike lists a tuple is immutable
Apart from that everything applicable to lists is applicable to tuples
'''

my_tuple = (1, 2, 3, 4, 5, 6)  # immutable. Once is created we cannot set/add/delete new values
print(my_tuple[1])
print(my_tuple[0:1])  # A tuple with a single item has a "," at the end!!!!
print(my_tuple[1:1])
print(my_tuple[1:2])  # A tuple with a single item has a ","  at the end!!!!
print(my_tuple[0:2])
print(my_tuple[0:4])
print(my_tuple.count(4))

'''
SET
Unordered collection of unique objects
'''

my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)
print(list(my_set))
my_set.add(100)
my_set.add(100)
my_set.add(2)
print(my_set)
print(3 in my_set)
my_set_union = my_set.union({7, 8, 9, 9, 10})
my_set_append = my_set | {7, 8, 9, 9, 10}
print(my_set)
print(my_set_union)
print(my_set_append)

my_list = [1, 2, 3, 4, 5, 5, 5]
print(my_list)
print(set(my_list))
