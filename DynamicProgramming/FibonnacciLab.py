def fibonacci(n):
    sequence = [0,1]

    if n < 1:
        return 0
    for i in range(2, n+1):
        sequence.append(sequence[i-1]+ sequence[i-2])
    return sequence[-1]

print(fibonacci(5))