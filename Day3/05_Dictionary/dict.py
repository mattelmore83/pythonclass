d = dict()

d.__setitem__('name','Chris') # long form
d['age'] = 25
d['cool'] = True

print(d)

d['age'] = 35

print(d)

print(d['cool'])

del d['cool']

print(d)

e = {
    'name': 'chris',
    'phone': '1234',
    'address': 'nowhere'
}

print(e)

'name' in e # determine if key value name exists in dict 'e' - run in REPL
len(e) # show length of dictionary - run in REPL

# >>> 'name' in e
# True
# >>> len(e)
# 3
# >>> type(e)
# <class 'dict'>

# loop through a dictionary - show keys
for i in e:
    print(i,e[i])