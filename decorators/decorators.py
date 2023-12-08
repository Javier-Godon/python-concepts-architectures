"""
decorators
"""

'''
decorators supercharge our functions
'''


def decorator_prototype(func):
    def wrap_func():
        func()

    return wrap_func


def decorator_one(func):
    def wrap_func():
        print('executing decorator one pre-function')
        func()
        print('executing decorator one post-function')

    return wrap_func


@decorator_one
def simple_function():
    print('simple function')


simple_function()


def decorator_two(func):
    def wrap_func(parameter, parameter2):
        print('executing decorator two pre-function')
        func(parameter, parameter2)
        print('executing decorator two post-function')

    return wrap_func


@decorator_two
def function_with_parameter(parameter, parameter2):
    print(parameter, parameter2)


function_with_parameter('string parameter', 'string parameter2')


def decorator_prototype_with_args(func):
    def wrap_func(*args, **kwargs):
        print('executing decorator proto two pre-function')
        func(*args, **kwargs)
        print('executing decorator proto two pre-function')

    return wrap_func


@decorator_prototype_with_args
def function_with_parameter_two(parameter, parameter2):
    print(parameter, parameter2)


function_with_parameter_two('string parameter', 'string parameter2')
