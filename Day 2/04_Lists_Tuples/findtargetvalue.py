
def get_target_value(g):
    i = 0
    target_value = 0
    for i in g:
        if i == "dog":
            target_value += 1
    return target_value

p = ["dog", "cat", "bird", "dog", "elephant", "tiger", "shark", "walrus", "dog"]
x = get_target_value(p)

print('Out of the following list:\n',p,'\nThe word dog appears',x,'times!')
