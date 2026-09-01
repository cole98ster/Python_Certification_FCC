def adjacency_list_to_matrix(dictionary: dict):
    length = len(dictionary)
    matrix = []

    index = 0
    for i in range(length):
        list_per_loop = []
        
        row = dictionary[index]
        for j in range(length):
            if j in row:
                list_per_loop.append(1)
            else:
                list_per_loop.append(0)
            
        print(list_per_loop)
        matrix.append(list_per_loop)
        index += 1
        
    return matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})