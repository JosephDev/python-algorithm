import random

def left(idx=None):
    return ((idx+1)<<1)-1

def right(idx=None):
    return (idx+1)<<1

def parent(idx=None):
    ((idx+1)>>1)-1

def max_heapify(arry=None, idx=None, heap_size=None):
    """
    LEFT: ((idx+1)<<1)-1
    RIGHT: (idx+1)<<1
    PARENT: ((idx+1)>>1)-1
    """
    l = left(idx)
    r = right(idx)
    
    if l <= heap_size and arry[l] > arry[idx]:
        largest = l
    else:
        largest = idx
    if r <= heap_size and arry[r] > arry[largest]:
        largest = r
    if largest != idx:
        arry[idx], arry[largest] = arry[largest], arry[idx]
        max_heapify(arry, largest, heap_size)

def build_max_heap(arry=None):
    heap_size = len(arry)-1
    for i in reversed(xrange(len(arry)//2)):
        max_heapify(arry, i, heap_size)

def heap_sort(heap=None):
    tmp_arry = list()
    for i in xrange(len(heap)):
        tmp_arry.append(heap.pop(0))
        max_heapify(heap, 0, len(heap)-1)
    return tmp_arry

if __name__ == "__main__":
    arry = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 12, 5, 3, 8, 2, 10, 33, 44, 7, 2, 8, 5, 4]
    build_max_heap(arry)
    print heap_sort(arry)
    