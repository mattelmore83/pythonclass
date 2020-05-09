
def get_average(g):
    i = 0
    sumList = 0
    listItems = 0
    for i in g:
        sumList = sumList + i
        listItems += 1
    return (sumList / listItems)


p = [5, 10, 15]

mean = get_average(p)

print('The average of the list is',mean)
