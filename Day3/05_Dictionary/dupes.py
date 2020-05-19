def find_dupes(data):
    newDict = {} # create a blank dictionary 'r'

    # create keys
    for item in data:
        newDict[item] = 0

    # increment counts
    for item in data:
        newDict[item] += 1

    return newDict

z = 'lkasdjflkjaflksdjfljsafs;;;;aklasjdflkj;;sfdakl'
print (find_dupes(z))

x = [1,1,1,2,2,2,2,3,3,4,4,5,6]
print (find_dupes(x))