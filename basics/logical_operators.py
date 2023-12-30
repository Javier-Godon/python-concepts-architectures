is_magician = False
is_expert = True

if is_expert and is_magician:
    print("You are an expert magician")

elif is_magician and not is_expert:
    print("in progress")

elif not is_magician:
    print("you need magic powers")

# == checks for equality
print(True == 1)  # print(True == bool(1))
print('' == 1)  # print(bool('') == bool(1))
print([] == 1)  # bool([] ==bool(1))
print(10 == 10.0)
print([] == [])
print('1' == 1)

# is checks for the location in memory
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print('1' is 1)
print(True is True)
print('1' is '1')
print([1, 2, 3] is [1, 2, 3])
