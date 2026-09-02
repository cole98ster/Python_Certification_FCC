def hanoi_solver(disks):
    rods = [list(range(disks, 0, -1)), [], []]
    output = []
    def record():
        output.append(" ".join(str(rod) for rod in rods))

    def solve(number, source, spare, destination):
        if number == 0:
            return

        solve(number - 1, source, destination, spare)

        rods[destination].append(rods[source].pop())
        record()

        solve(number - 1, spare, source, destination)

    record()
    solve(disks, 0, 1, 2)
    
    final_output = "\n".join(output)
    return final_output


print(hanoi_solver(3))