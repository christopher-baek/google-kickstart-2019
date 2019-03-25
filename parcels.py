def manhattan_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def solve(world):
    offices = []

    for row in range(len(world)):
        for col in range(len(world[row])):
            if world[row][col] == 1:
                offices.append((row, col))

    distances = []

    for row in range(len(world)):
        mins = []
        for col in range(len(world[row])):
            mins.append(
                min([manhattan_distance(row, col, o[0], o[1]) for o in offices]))
        distances.append(mins)

    max_so_far = 0
    max_row = None
    max_col = None

    for row in range(len(distances)):
        for col in range(len(distances[row])):
            if distances[row][col] > max_so_far:
                max_row = row
                max_col = col
                max_so_far = distances[row][col]

    if max_so_far == 0:
        return 0

    offices.append((max_row, max_col))
    new_distances = []
    for row in range(len(world)):
        mins = []
        for col in range(len(world[row])):
            mins.append(
                min([manhattan_distance(row, col, o[0], o[1]) for o in offices]))
        new_distances.append(mins)

    new_max_so_far = 0

    for row in range(len(new_distances)):
        for col in range(len(new_distances[row])):
            if new_distances[row][col] > new_max_so_far:
                new_max_so_far = new_distances[row][col]

    return new_max_so_far


def main():
    """
    - 1 <= t <= 100
    """
    t = int(input())

    for test_case_index in range(t):
        r_and_c = input()
        r_and_c = r_and_c.split(' ')
        r = int(r_and_c[0])
        c = int(r_and_c[1])

        world = []
        for x in range(r):
            cols = input()
            world.append([int(cols[y]) for y in range(len(cols))])

        print('Case #{}: {}'.format(test_case_index + 1, solve(world)))


if __name__ == '__main__':
    main()
