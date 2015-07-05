import random

def insert_sort(array):
    for i in xrange(len(array)):
        if i > 0:
            while array[i-1] >= array[i] and i > 0:
                array[i-1], array[i] = array[i], array[i-1]
                i = i-1

if __name__ == "__main__":
    array = [int(random.uniform(1, 50)) for i in xrange(10)]
    insert_sort(array)
    print array