def sum_two_numbers():
    """
    this function returns a function that sums two numbers
    :return: inner_function
    """

    def inner_function(num1, num2):
        return num1 + num2

    return inner_function


returned_function = sum_two_numbers()
print(returned_function)
print(returned_function(5, 10))


def sum_two_numbers_v2(num1, num2):
    """
    this function returns the sum of two numbers
    :return: num1 + num2
    """

    def inner_function_v2(first_number, second_number):
        return first_number + second_number

    return inner_function_v2(num1, num2)


print(sum_two_numbers_v2(5, 10))

'''
Methods vs Functions
'''
# Functions:
print('CALLING FUNCTION Print')
# input('ASKING YOU TO ENTER SOMETHING FROM FUNCTION Input')

# Methods: a method has to be owned by something
# (They are related to classes. So they are functions defined in classes)
'hello'.capitalize()

print('***************with help************************')
help(sum_two_numbers)
print('****************printing the doc****************')
print(sum_two_numbers.__doc__)

'''
*args **kwargs
*args inside of a function is a tuple of those arguments
**kwargs allows us to use keyword arguments
'''


def super_function(*args):
    print('summing arguments')
    print(*args)
    print('this prints the arguments as a tuple')
    print(args)
    return sum(args)


print(super_function(1, 2, 3, 4))


def super_function_v2(*args, **kwargs):
    print('summing arguments')
    print(*args)
    # print(**kwargs)
    print('this prints the arguments as a tuple')
    print(args)
    print('this prints the keyword arguments as a dictionary')
    print(kwargs)
    print(kwargs.values())
    return sum(args) + sum(kwargs.values())


def sum_values_in_dictionary(dictionary: dict) -> int:
    total = 0
    for items in dictionary.values():
        total += items
    return total


print(super_function_v2(1, 2, 3, 4, num1=5, num2=10))

'''
RULE: The order must be: params, *args, default parameters, **kwargs
'''


def full_parameters(param1, *args, param4='default', **kwargs):
    print('******************************FULL PARAMETERS********************************')
    print(param1)
    print(*args)
    print(param4)
    print(kwargs)


full_parameters('param1', 'param2', 'param3', num1=5, num2=10)


def highest_even(input_list):
    even_list = filter(is_even, input_list)
    return max(even_list)


def is_even(number: int):
    return number % 2 == 0


print(highest_even([10, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))

variable = 'toooo lo000ng'
if len(variable) > 8:
    print(f'too long {len(variable)} elements')
'''
using := (Walrus operator)
it assigns values to variables as part of a larger expression
'''
if (n := len(variable)) > 8:
    print(f'too long {n} elements')
