# Reference powerpoint "snippets1.pptx"

def helper():
    print("HA!")
    print("Why")

def say_hi():
    helper()
    print("Hello")
    print("There")

def say_bye():
    helper()
    print("Bye")
    print("bye")

def come_and_go():
    say_hi()
    print('>>> This is the middle')
    say_bye()

print('>>> Start')
come_and_go()
print('>>> Done')