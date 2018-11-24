
def binSearch(alist, item):
    index = 0
    lastIndex = len(alist)-1
    foundIt = -1
    while index <= lastIndex and foundIt == -1:
        midpoint = (index + lastIndex)//2 
        if alist[midpoint] == item:
            foundIt = midpoint
        else:
            if item < alist[midpoint]:
                lastIndex = midpoint - 1
            else:
                index = midpoint + 1
    return foundIt

