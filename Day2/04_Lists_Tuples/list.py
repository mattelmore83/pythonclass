
# create a new list
p = list()

# Things you can do with a list
# sort
# add
# loop/iterate through it

# append - sticks something to the end of the list
p.append(5) #0
p.append('hello') #1
p.append(True) #2

# determine size of list
x = p.__len__()
print('Your list has this many items: ',x)

# read a specific item from a list
# can use negative indices to start at the end of the list
#x = p.__getitem__(2)
x = p[2]
print('Item number two in this list is: ',x)

# set a specific item in a list
#p.__setitem__(0,500)
p[0]=500

# insert an item into the list at a specific index
p.insert(2,'world')

# delete an item
#p.__delitem__(3)

# determine length
length = p.__len__()
print('The length of the list is ',length)

# make a representation of the list
x = p.__repr__()
print('Here\'s the full list:\n',x)