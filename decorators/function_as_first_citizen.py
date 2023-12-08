def do_something():
    print("doing something")


variable = do_something
del do_something

print(variable())


def first_function(func):
    func()


def second_function():
    print("second function")


print(first_function(second_function))

'''
High order function: HOC
- function that accepts another function
- function that returns another function
Ex: map(func, *iterables), reduce(), filter(),...

'''


def accepts_another_function(func):
    func()


def returns_another_function():
    def func():
        return 5

    return func

