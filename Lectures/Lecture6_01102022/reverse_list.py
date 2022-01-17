
import copy 
def max_value(arr):
    maximum = -999
    for i in range(len(arr)):
        if maximum <= arr[i]:
            maximum = arr[i]
    return maximum

def reverse_list(list):
    reversed_list = []
    cp = copy.deepcopy(list)
    while len(cp) > 0:
        maximum = max_value(cp)
        reversed_list.append(maximum)
        cp.remove(maximum)
        print(reversed_list)
    return reversed_list

arr = [1, 2, 3, 4 , 5]
reverse_list(arr)