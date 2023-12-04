import time
import random

def split(data_list):
    mid_ind = len(data_list)//2
    if mid_ind == 0:
        return data_list
    left_list = split(data_list[:mid_ind])
    right_list = split(data_list[mid_ind:])
    return merge_list(left_list, right_list)

def merge_list(left, right):
    final_list = []
    while left and right:
        left_value = left[0]
        right_value = right[0]
        if left_value <= right_value:
            left = left[1:]
            final_list.append(left_value)
        else:
            right = right[1:]
            final_list.append(right_value)
    if left:
        final_list += left
    else:
        final_list += right
    return final_list


data_set = []
for i in range(1_000):
    data_set.append(random.randint(1, 1_000))

start = time.time()

split(data_set)

end = time.time()
time = (end - start) * 1000
print(time)
