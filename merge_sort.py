import random

def merge_sort(array):
    if len(array) >1:
        left_array = array[:len(array)/2]
        right_array = array[len(array)/2:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_idx = 0
        right_idx = 0

        for i in xrange(len(array)):
            left_idx = left_idx if left_idx < len(left_array) else None
            right_idx = right_idx if right_idx < len(right_array) else None

            if left_idx is None:
                array[i] = right_array[right_idx]
                right_idx += 1
            elif right_idx is None:
                array[i] = left_array[left_idx]
                left_idx += 1
            elif left_idx is not None and right_idx is not None and left_array[left_idx] <= right_array[right_idx]:
                array[i] = left_array[left_idx]
                left_idx += 1
            else:
                array[i] = right_array[right_idx]
                right_idx += 1

if __name__ == "__main__":
    array = [int(random.uniform(1, 50)) for i in xrange(11)]
    merge_sort(array)
    print array
    