import random

def bubble_sort(array):
    for i in xrange(len(array)):
        for x in xrange(len(array)-i-1):
            if array[x+1] < array[x]:
                array[x+1], array[x] = array[x], array[x+1]


if __name__ == "__main__":
    array = [int(random.uniform(1, 50)) for i in xrange(10)]
    bubble_sort(array)
    print array