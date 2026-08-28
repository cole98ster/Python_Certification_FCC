def square_root_bisection(num, tolerance = 1e-7, iterations = 50):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    low = 0.0
    high = max(1.0, float(num))
    root = None
    for x in range(iterations):
        mid = (low + high) / 2
        square = mid * mid
        
        if square > num:
            high = mid
        else: 
            low = mid
        
        if high - low <= tolerance:
            root = (low + high) / 2
            break


    if root is None:
        print(f"Failed to converge within {iterations} iterations")
        return None

    print(f"The square root of {num} is approximately {root}")
    return root

result = square_root_bisection(0.001, 1e-7, 50)
print("result:", result)