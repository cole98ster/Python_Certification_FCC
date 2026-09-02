def range_of_numbers(start_num,end_num):
    if end_num == start_num:
        return [start_num]
    
    list_of_numbers = range_of_numbers(start_num, end_num-1)
    
    list_of_numbers.append(end_num)
    return list_of_numbers

print(range_of_numbers(3, 9))