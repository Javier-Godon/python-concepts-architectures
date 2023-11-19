def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


def get_hello(first_name, last_name):
    return f"Hello {first_name} {last_name}"


def increment_with_default(base_number: int, increment: int = 1):
    return base_number + increment


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user)
    print(user['first_name'])


def fizz_buzz(selected_number):
    if (selected_number % 3 == 0) and (selected_number % 5 == 0):
        return "FizzBuzz"
    if selected_number % 3 == 0:
        return "Fizz"
    if selected_number % 5 == 0:
        return "Buzz"
    return selected_number
