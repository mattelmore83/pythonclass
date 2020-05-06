def add_two(a, b):
    c = a + b
    return c  ### Allows this variable to be exported of the function
    ### All functions return something - if not defined, then 'None' is returned


x = add_two(3, 4)
print(x)
