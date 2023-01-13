with open("9.txt") as file:
    inp = [row.strip() for row in file.readlines()]

import numpy as np

head = (0, 0)
tail = (0, 0)
visited = set()
visited.add(tail)

for motion in inp:
    direction, steps = motion.split()
    for _ in range(int(steps)):
        match direction:
            case 'U':
                head = (head[0], head[1] + 1)
            case 'D':
                head = (head[0], head[1] - 1)
            case 'R':
                head = (head[0] + 1, head[1])
            case 'L':
                head = (head[0] - 1, head[1])
        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]
        if abs(diff_x) > 1 or abs(diff_y) > 1:
            tail = (tail[0] + np.sign(diff_x), tail[1] + np.sign(diff_y))
            visited.add(tail)
print(len(visited))


