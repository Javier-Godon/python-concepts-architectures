is_old = True
is_licensed = False
other_condition = True
fourth_condition = False
if is_old and is_licensed:
    print("Old enough and has a license")
elif not other_condition:
    print("not other condition ")
elif fourth_condition:
    print("Fourth condition")
else:
    print('not allowed')

''' Truthy and Falsy
All values are considered Truthy except: None, False, 0, 0.0, 0j, Decimal(0), [], {}, (),'',b'',set(), range(0)
'''
truthy_value = bool('hi')
print(truthy_value)
truthy_value = bool(10)
print(truthy_value)

falsy_value = bool('')
print(falsy_value)
falsy_value = bool(0)
print(falsy_value)

# a possible use is to check if some values have a value (they are filled)
password = 'pass'
username = 'username'
if password and username:
    print('Password and username have been entered')

'''
Ternary operator: condition_if_true if condition else condition_if_else
'''

is_friend=True
can_message = "message allowed" if is_friend else "message not allowed"
print(can_message)


