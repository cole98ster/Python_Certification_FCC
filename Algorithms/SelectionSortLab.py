def selection_sort(array):
    length = len(array)
    iterate = 0
    while iterate < length:
        smallest_x = array[iterate]
        index_smallest = iterate
        for index, x in enumerate(array[iterate:]):
            
            if x < smallest_x:
                smallest_x = x
                index_smallest = index + iterate
        if index_smallest != iterate:
            array[iterate],array[index_smallest] = array[index_smallest], array[iterate]

        iterate += 1
    return array
