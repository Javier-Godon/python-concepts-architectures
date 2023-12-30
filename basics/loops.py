for item in 'iterate':
    print(item)

for item in [1, 2]:
    print(item)
    print(item)
print(item)

for item_a in (1, 2, 3):
    for item_b in ['a', 'b', 'c']:
        print(item_a, item_b)

user = {
    'first_name': 'Javier',
    'last_name': 'Godon',
    'email': 'email@example.com',
    'age': 33,
    'can_swing': True
}
for item in user:
    print(item)
for item in user.items():
    print(item)
for item in user.values():
    print(item)
# we can collect key, value pair in a dictionary
for key, value in user.items():
    print(key, value)
for number in range(0, 10):
    print(number)

for _ in range(0, 10):
    print("doing something, and I don't need a variable")

for _ in range(10, 0, -2):
    print(_)

for _ in range(2):
    print(list(range(10)))

for i, char in enumerate(['a', 'b', 'c']):
    print(i, char)

'''
while
'''
counter = 0
while counter < 10:
    print(f"counting: {counter}")
    counter += 1
else:
    print("done")

counter = 0
while counter < 10:
    print(f"counting: {counter}")
    if counter == 6:
        break
    counter += 1
else:  # it is executed only when the condition gets to false
    print("done")

while True:
    response = input('input something: ')
    if response == 'bye':
        break

test_list = ['one', 'two', 'three', 'four', 'five']
for item in test_list:
    continue

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        if pixel == 1:
            print('*', end='')
    print('')

# Check for duplicates in list:
test_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
set_checker = set()
duplicates_list = []
for item in test_list:
    if item in set_checker:
        duplicates_list.append(item)
    set_checker.add(item)

print(duplicates_list)

duplicates_list.clear()
for item in test_list:
    if test_list.count(item) > 1 and item not in duplicates_list:
        duplicates_list.append(item)

print(duplicates_list)
