
def read_byte():
    print('Reading byte')
    a = 0
    #a = 1/0
    print('Got the byte back from the drive')
    return a

def read_word():
    print('Reading a word')
    a = read_byte()
    b = read_byte()
    print('Got the word')
    return a*256 + b

def read_long():
    print('Reading a long')
    a = read_word()
    b = read_word()
    print('Got the long')
    return a*65536+b

print('Start')
try:
    print('I am here')
    a = read_long()
    #a = 1/0
    print('And here')
except Exception as e:
    print('Error',e)
else:
    print('Nothing bad happened')
finally:
    print('All done')