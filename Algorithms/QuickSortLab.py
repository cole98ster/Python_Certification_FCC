def quick_sort(array):
    if not array:
        return []
    if len(array) == 1:
        return array
    pivot = array[0]
    left_list = []
    right_list = []
    equal_list = []
    for x in array:
        if x < pivot:
            left_list.append(x)
        elif x == pivot:
            equal_list.append(x)
        else:
            right_list.append(x)
    left_list = quick_sort(left_list)
    right_list = quick_sort(right_list)
    returned_array = left_list + equal_list + right_list
    return returned_array
