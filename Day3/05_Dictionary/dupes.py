def find_dupes(d):
    r = {} # create a blank dictionary 'r'

    # create keys
    for i in d:
        r[i] = 0

    # increment counts
    for i in d:
        r[i] += 1

    return r

z = 'lkasdjflkjaflksdjfljsafs;;;;aklasjdflkj;;sfdakl'
print (find_dupes(z))

x = [1,1,1,2,2,2,2,3,3,4,4,5,6]
print (find_dupes(x))