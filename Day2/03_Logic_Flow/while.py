
a = 0

while a<10:
    a = a + 1
    if a == 10:
        print('Made it to ten! ',a)
        break # takes you out of the loop
#       continue # takes you back to the top of the loop
    print('Not ten yet...',a) # not run if continue is executed from above line