

lista = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
        [21], [22], [23], [24], [25]]



def binarySearch(lista):
    flattened = [val for sublist in lista for val in sublist]
    first = 0
    last = len(flattened)-1
    found = False
    item = int(input('digite o item: '))
    while first <= last and not found:
        midpoint = int((first + last)//2)
        if flattened[midpoint] == item:
            found = True
        else:
            if item < flattened[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return print(found)


binarySearch(lista)

