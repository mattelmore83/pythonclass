# find the largest item in a list
def find_max(my_data):
    max_val = my_data[0]
    for i in my_data:
        if i>max_val:
                max_val = i
    return max_val

p = [1,6,7,33,42,50,-8]

x = find_max(p)

print(x)