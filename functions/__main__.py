from functions.function_definitions import hello, get_hello, increment_with_default, multiply, save_user, fizz_buzz

hello("Javier", "Godón")
print(get_hello("Peter", "Brown"))
hello(first_name="Michael", last_name="Jackson")

print(increment_with_default(base_number=20))
print(increment_with_default(base_number=20, increment=55))

print(multiply(2, 3, 4, 5))

save_user(first_name="Javier", last_name="Godon")

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(31))
