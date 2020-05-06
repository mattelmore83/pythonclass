def say_hi():
    global a
    a = 8
    print(a)
# Can use "global a" to tell compiler to always use the locally defined 'a' globally

a = 5

say_hi()
print(a)
