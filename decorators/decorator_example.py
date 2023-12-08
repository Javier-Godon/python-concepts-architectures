from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'it took {end - start} s')
        return result

    return wrapper


@performance
def long_time_to_complete_function():
    for i in range(100_000_000):
        var = i * 5


long_time_to_complete_function()
