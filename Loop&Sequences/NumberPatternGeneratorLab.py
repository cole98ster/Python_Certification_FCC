def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    index = 0
    string = ''
    while index < n:
        index += 1 
        if index == n:
            string += str(index)
            break
        string += str(index)+ ' '
    return string



test = number_pattern(4)
print(test)