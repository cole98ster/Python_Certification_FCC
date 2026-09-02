def dfs_n_queens(n):
    if n < 1:
        return []
    
    result = []
    board = [-1] * n
    row = 0
    
    while row >= 0 and row < n:
        found_safe = False
        start_col = board[row] + 1 if board[row] >= 0 else 0
        
        for col in range(start_col, n):
            is_safe = True
            for prev_row in range(row):
                prev_col = board[prev_row]
                if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                    is_safe = False
                    break
            
            if is_safe:
                board[row] = col
                found_safe = True
                break
        
        if found_safe:
            if row == n - 1:
                result.append(board[:])
                board[row] = -1
                row -= 1
            else:
                row += 1
        else:
            board[row] = -1
            row -= 1
    
    return result
    

