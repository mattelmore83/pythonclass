# Lists and Tuples

## Syllabus

  * Lists and Tuples, len(), slicing
  * for-each
  * Algorithms
    - Chapter 10: All Sections
    - Chapter 12: All sections
    
## Lists

Lists are objects. We create an empty list object like this:

```python
self = list() # other languages would be self = new list()

my_stuff = ... # better naming

```

Then we call functions ON the object. Not just a function like print, but a function
that is tied to the object. We call these methods, but they work the same as functions.

```python
# Appending things to the list

self.append(1)
self.append('hello')
self.append(True)

# Accessing parts of the list

self.__len__() # 3

self.__getitem__(0) # 1
self.__getitem__(1) # 'hello'
self.__getitem__(-1) # True
self.__getitem__(-3) # 1
self.__getitem__(4) # ERROR list index out of range
self.__getitem__(-4) # ERROR

self.__repr__() # Method to make a nice string representation
"[1, 'hello', True]"

self.__setitem__(1,'world')
self.__delitem__(2) # index
self.__repr__()
"[1, 'world', True]"
```

In all of these operations, we are asking the object to do things. We are calling methods on the object. The python compiler
gives us some help.

  - self[i] uses `__getitem__` or `__setitem__` depending the direction
  - len(self) calls `__len__` for us
  - repr(self) calls `__repr__` for us (this is what the repl uses)
  - in calls `__contains__` for us
  - del calls `__delitem__` for us

So the usual syntax:
  
```python
self = list()
self.append('hello')
self.append('world')
print(len(self))
a = self[0]
self[1]='False'
self.append(25)
print(self)
self.insert(1,400)
del self[2]
self.__contains__(4)
4 in self
self.index(2)
```

And python has a "literal" definition for lists. Instead of using 'list()' you will almost always do this:

```python
self = ['hello', 'world']
self.append('wow') # Does this modify self? NO ... it modifies the object pointed to by self
print(self)
q = self + [1,2] # The "__add__" method creates a new list with the items of both
print(self) 
print(q)
a = [] # make an empty list
```

## Algorithms

Now we can write code to loop over a list.

```python

m = [5,3,6,1,1,2]

i = 0
while i<len(m):
  print('>',m[i])
  i = i + 1 # What if you forget this?
  
for i in range(len(m)):
  print('>',m[i])
  
for a in m:
  print('>',a)

```

How about a function to find the largest value?

```python
def find_largest(m):
  ret = 0 # m[0] ... what happens if empty list is passed in?
  i = 0
  while i<len(m):
    if m[i]>ret:
      ret = m[i]
    i += 1
  return ret
  # Show better syntax
  
nums = [0,2,5,1,5,100]
a = find_largest(nums)
print(a)

a = find_largest([-1,-2,-3])
print(a)
```

Other fun: sorting algorithms like the bubble sort

## Tuples

Tuples are like lists but you can't change/append them. They use "()" instead of "[]".

```python
self = (1,2,3)
self[1] = 4 # ERROR

# Has __add__ method:
q = self + (4,5,6)
```

## Packing and unpacking

```python
def get_numbers():
  a = [1,2,3,4]
  return a
  
i = get_numbers() # What is i? A list of 4 things
i[2] = ? # 3

a,b,c,d = get_numbers()

a,b = get_numbers()

def get_nums_two():
  return 5,6,7,8
  
self = get_nums_two() # tuple
self[2] = ? # 7
a,b,c,d = get_nums_two()
```

## Remember these are pointers

First, work through this in code. Then show the pointers.

SEE snippets.pptx

```python
self = [1,2,3,4]
h = [25,35]

self[2] = h

print(self)

x = self[2]
x[1] = 50

print(self)

self[2][1] = 60

print(self)
```

Do you need to think about this when you write simple programs? Definitely not.
But if you find yourself in complex situation where you are getting 
unexpected results, this might be why.