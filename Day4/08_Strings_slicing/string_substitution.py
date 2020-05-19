
def sub_key_value(s,key,value):
    r = s.replace('<<'+key+'>>',value)
    return r

def substitute(s,data):
    for key in data:
        value = data[key]
        s = s.replace('<<'+key+'>>',value)
    return s


a = 'Hello <<NAME>>. I hear you like <<FOOD>> and have a pet <<ANIMAL>>.'

#a = sub_key_value(a,'NAME','Matt')
#a = sub_key_value(a,'FOOD','Steak')
#a = sub_key_value(a,'ANIMAL','dog')
#print(a)

v = {
    'NAME' : 'Matt',
    'FOOD' : 'steak',
    'ANIMAL' : 'dog'
}

print(substitute(a,v))