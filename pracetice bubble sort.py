def bubble_sort(items,comp=lambda x,y:x>y):
    items=items[:]
    for i in range(len(items)-1):
        swapped=False
        for i in range(len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1]=items[j+1],items[j]
                swapped=True
        if not swapped:
            break
    return items
