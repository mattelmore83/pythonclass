try:
    print('I am here')

    #a = 1 / 0  # raises an exception that is unhandled, so program is terminated unless there is an exception handler
    #a = akjsdfjlkjadfs
    #a = 1 / notanumber

    print('and I am here')

except ZeroDivisionError as e:
    print('cant divide by zero:',e)

except IndexError as e:
    print('index error:',e)

except NameError as e:
    print('name error:',e)

except TypeError as e:
    print('type error:',e)

except Exception as e:
    print('that was bad:',e)

print('bye bye now!')
