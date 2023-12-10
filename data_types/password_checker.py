user = input('Please enter your username')
passw = input('Please enter your password')

hidden_password = '*' * len(passw);
print(f'{user} Your password is {hidden_password}')
