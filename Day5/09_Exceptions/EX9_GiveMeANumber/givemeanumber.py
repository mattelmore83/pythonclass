def get_number():
    while True:
        user_input = input('Give me a number between 1 and 100: ')
        try:
            user_input = int(user_input)
            if user_input > 100 or user_input < 1:
                print('That\'s not between 1 and 100!')
            else:
                return user_input
        except Exception as e:
            print('That is not a number! Error:',e)

a = get_number()
print('You gave me', a)
