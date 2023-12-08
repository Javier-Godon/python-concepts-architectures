import collections
from copy import deepcopy, copy
from pprint import pprint

scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
    {'name': 'Marie Curie', 'field': 'physics', 'born': 1867, 'nobel': True},
    {'name': 'Tu Youyou', 'field': 'chemistry', 'born': 1930, 'nobel': True},
    {'name': 'Ada Yonath', 'field': 'chemistry', 'born': 1939, 'nobel': True},
    {'name': 'Vera Rubin', 'field': 'astronomy', 'born': 1928, 'nobel': False},
    {'name': 'Sally Ride', 'field': 'physics', 'born': 1951, 'nobel': False}
]

simple_copy = copy(scientists)
deep_copy = deepcopy(scientists)

scientists[0]['name'] = 'changed'
print(scientists)
print(simple_copy)
print(deep_copy)

# namedtuple are immutable
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])
ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)
print(ada)
ada_copy = Scientist._make(ada)
print(ada_copy)

scientists_as_list = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)
]

# I am still able to delete items, even each one of them is immutable
del scientists_as_list[0]
pprint(scientists_as_list)

scientists_as_tuple = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)
)

pprint(scientists_as_tuple)
pprint(scientists_as_tuple[0].name)
