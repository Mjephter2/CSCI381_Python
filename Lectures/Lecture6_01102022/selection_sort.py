import random
unsorted = []
for i in range(100):
    unsorted.append(random.randint(-100, 100))

def min_value(arr):
    minimum = 999
    for i in range(len(arr)):
        if minimum >= arr[i]:
            minimum = arr[i]
    return minimum

def select_sort(arr):
    sorted_list = []
    while len(arr) > 0:
        m = min_value(arr)
        sorted_list.append(m)
        arr.remove(m)
    return sorted_list

print(select_sort(unsorted))