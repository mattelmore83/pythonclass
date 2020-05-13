
def get_average(g):
    i = 0
    sumList = 0
    listItems = 0
    for i in g:
        sumList = sumList + i
        listItems += 1
    #return (sumList / listItems)   #### can also use len(d) instead of listItems being manually counted
    return sumList / len(g)

p = [5, 10, 15, 69]

mean = round(get_average(p))

print('The average of the list is',mean)
