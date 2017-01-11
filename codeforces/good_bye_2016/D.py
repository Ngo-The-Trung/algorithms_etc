import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
a = [int(x) for x in lines[1].split(" ")]

dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
]

cells = set()

cur = [
    ((0,0), -1)
]

for i in range(n):
    new_cur = []

    for fork in cur:
        coord, pos = fork
        direction = dirs[pos]
        for j in range(a[i]):
            coord = (coord[0] + direction[0], coord[1] + direction[1])
            cells.add(coord)

        dir_left = (pos - 1) % 8
        dir_right = (pos + 1) % 8
        new_cur.append((coord, dir_left))
        new_cur.append((coord, dir_right))

    cur = new_cur
print len(cells)
